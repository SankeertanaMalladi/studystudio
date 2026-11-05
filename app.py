from functools import wraps
import random
import secrets
import os

from flask import Flask, flash, redirect, render_template, request, session, url_for

from course_content import COURSES, get_course
from database.database import (
    create_database, get_course_stats, get_enrollments, get_recent_results,
    login_user, record_quiz_result, register_user, save_enrollments,
)

app = Flask(__name__)
app.secret_key = os.environ.get("STUDY_STUDIO_SECRET", "study_studio_dev_key_change_for_production")
ACTIVE_QUIZZES = {}
create_database()


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped


@app.route("/")
def index():
    return redirect(url_for("dashboard" if "user_id" in session else "login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = login_user(request.form.get("username", ""), request.form.get("password", ""))
        if user:
            session.clear()
            session["user_id"] = user["id"]
            session["username"] = user["full_name"]
            return redirect(url_for("dashboard"))
        return render_template("login.html", error="That username and password did not match.")
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("fullname", "").strip()
        email = request.form.get("email", "").strip()
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if len(password) < 8:
            return render_template("register.html", error="Use a password with at least 8 characters.")
        if not all((name, email, username)):
            return render_template("register.html", error="Please complete every field.")
        if not register_user(name, email, username, password):
            return render_template("register.html", error="That username or email is already registered.")
        user = login_user(username, password)
        session["user_id"] = user["id"]
        session["username"] = user["full_name"]
        return redirect(url_for("courses"))
    return render_template("register.html")


@app.route("/dashboard")
@login_required
def dashboard():
    user_id = session["user_id"]
    enrolled_ids = get_enrollments(user_id)
    my_courses = [COURSES[cid] for cid in enrolled_ids if cid in COURSES]
    recent = get_recent_results(user_id)
    for result in recent:
        course = get_course(result["course_id"])
        result["course_title"] = course["title"] if course else result["course_id"]
        result["percent"] = round(100 * result["score"] / result["total"])
    attempts = sum(get_course_stats(user_id, cid)["attempts"] for cid in enrolled_ids)
    return render_template(
        "dashboard.html", username=session["username"], courses=my_courses,
        recent=recent, attempts=attempts, course_count=len(my_courses),
        active_page="dashboard",
    )


@app.route("/courses")
@login_required
def courses():
    selected = set(get_enrollments(session["user_id"]))
    return render_template(
        "courses.html", courses=COURSES, selected=selected,
        categories=sorted({course["category"] for course in COURSES.values()}),
        active_page="courses",
    )


@app.route("/enroll", methods=["POST"])
@login_required
def enroll():
    picked = [cid for cid in request.form.getlist("course_ids") if cid in COURSES]
    save_enrollments(session["user_id"], picked)
    flash("Your learning plan has been updated.")
    return redirect(url_for("dashboard"))


@app.route("/course/<course_id>")
@login_required
def course_detail(course_id):
    course = get_course(course_id)
    if not course:
        return redirect(url_for("courses"))
    stats = get_course_stats(session["user_id"], course_id)
    enrolled = course_id in get_enrollments(session["user_id"])
    return render_template(
        "course.html", course=course, stats=stats, enrolled=enrolled,
        active_page="courses",
    )


@app.route("/enroll/<course_id>", methods=["POST"])
@login_required
def enroll_one(course_id):
    if course_id not in COURSES:
        return redirect(url_for("courses"))
    current = get_enrollments(session["user_id"])
    if course_id not in current:
        current.append(course_id)
        save_enrollments(session["user_id"], current)
    flash("Course added to your learning plan.")
    return redirect(url_for("course_detail", course_id=course_id))


@app.route("/flashcards/<course_id>")
@login_required
def flashcards(course_id):
    course = get_course(course_id)
    if not course:
        return redirect(url_for("courses"))
    return render_template("flashcards.html", course=course, active_page="courses")


@app.route("/quiz/<course_id>")
@login_required
def quiz(course_id):
    course = get_course(course_id)
    if not course:
        return redirect(url_for("courses"))
    if course_id not in get_enrollments(session["user_id"]):
        return redirect(url_for("course_detail", course_id=course_id))

    mode = request.args.get("mode", "practice")
    if mode not in ("practice", "mock"):
        mode = "practice"
    bank = course["questions"]
    count = min(len(bank), 5 if mode == "practice" else 10)
    picked = random.sample(bank, count)
    rendered = []
    answers = []
    for item in picked:
        choices = list(item["choices"])
        correct_text = choices[item["answer"]]
        random.shuffle(choices)
        answers.append(choices.index(correct_text))
        rendered.append({
            "topic": item["topic"],
            "question": item["question"],
            "choices": choices,
        })

    quiz_id = secrets.token_urlsafe(24)
    ACTIVE_QUIZZES[quiz_id] = {
        "user_id": session["user_id"], "course_id": course_id,
        "mode": mode, "answers": answers, "questions": picked,
    }
    return render_template(
        "quiz.html", course=course, questions=rendered, quiz_id=quiz_id,
        mode=mode, active_page="courses",
    )


@app.route("/submit-quiz", methods=["POST"])
@login_required
def submit_quiz():
    quiz = ACTIVE_QUIZZES.pop(request.form.get("quiz_id", ""), None)
    if not quiz or quiz["user_id"] != session["user_id"]:
        flash("That quiz has expired. Please start a new one.")
        return redirect(url_for("dashboard"))

    total = len(quiz["answers"])
    score = sum(
        request.form.get(f"q{i}") == str(answer)
        for i, answer in enumerate(quiz["answers"])
    )
    percent = round(100 * score / total)
    record_quiz_result(
        session["user_id"], quiz["course_id"], quiz["mode"], score, total
    )
    course = get_course(quiz["course_id"])
    if percent >= 85:
        feedback = "Strong command of these concepts. Try a harder application or explain the ideas in your own words."
    elif percent >= 60:
        feedback = "Good progress. Review the missed concepts, then try another short practice set."
    else:
        feedback = "Start with the foundations below. Use a flashcard round, revisit the materials, and retry when ready."
    review = []
    for i, item in enumerate(quiz["questions"]):
        if request.form.get(f"q{i}") != str(quiz["answers"][i]):
            review.append({
                "question": item["question"],
                "answer": item["choices"][item["answer"]],
                "explanation": item["explanation"],
            })
    return render_template(
        "result.html", course=course, score=score, total=total, percent=percent,
        feedback=feedback, review=review, mode=quiz["mode"], active_page="courses",
    )


@app.route("/guidance/<course_id>", methods=["GET", "POST"])
@login_required
def guidance(course_id):
    course = get_course(course_id)
    if not course:
        return redirect(url_for("courses"))
    stats = get_course_stats(session["user_id"], course_id)
    latest = next(
        (r for r in get_recent_results(session["user_id"], 30) if r["course_id"] == course_id),
        None,
    )
    score = round(100 * latest["score"] / latest["total"]) if latest else None
    hours = 5
    goal = "Build a confident foundation"
    plan = []
    if request.method == "POST":
        goal = request.form.get("goal", goal).strip()[:120] or goal
        try:
            hours = max(2, min(20, int(request.form.get("hours", 5))))
        except ValueError:
            hours = 5
        focus = "Revisit the core concepts and use short recall sessions." if score is not None and score < 60 else "Mix retrieval practice with small hands-on applications."
        sessions = [
            ("Day 1", f"{focus} Review 2 flashcard rounds."),
            ("Day 2", "Study one course resource and write a short summary."),
            ("Day 3", "Complete a practice quiz and explain each answer."),
            ("Day 4", "Apply the week's ideas in a small example or mini-project."),
            ("Day 5", "Review mistakes and choose one concept to strengthen."),
        ]
        plan = sessions[:max(2, min(5, hours // 2))]
    return render_template(
        "guidance.html", course=course, stats=stats, latest_score=score,
        hours=hours, goal=goal, plan=plan, active_page="courses",
    )


@app.route("/home")
def legacy_home():
    return redirect(url_for("dashboard"))

@app.route("/analyze")
def legacy_analyze():
    return redirect(url_for("courses"))

@app.route("/submit_quiz", methods=["GET"])
def legacy_submit_page():
    return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
