from utils.feedback import generate_feedback
from utils.recommendation import materials
from utils.study_plan import generate_plan


def generate_report(subject, quiz_score, level, learning_style):
    if quiz_score >= 85:
        performance = "Excellent"
    elif quiz_score >= 70:
        performance = "Good"
    elif quiz_score >= 50:
        performance = "Average"
    else:
        performance = "Needs Improvement"

    difficulty = (
        "Hard" if performance == "Excellent"
        else "Medium" if performance in ("Good", "Average")
        else "Easy"
    )
    resources = materials[materials["Subject"] == subject]
    selected = resources[resources["Difficulty"] == difficulty]
    if selected.empty:
        selected = resources
    selected = selected.head(5)

    feedback = generate_feedback(performance, quiz_score)
    feedback.append(f"Your selected learning style is {learning_style}.")

    return {
        "subject": subject,
        "level": level,
        "performance": performance,
        "quiz_score": quiz_score,
        "resources": [
            {
                "title": row["Resource_Name"],
                "description": row["Description"],
                "url": row["Resource_Link"],
            }
            for _, row in selected.iterrows()
        ],
        "feedback": feedback,
        "study_plan": generate_plan(subject, performance),
    }
