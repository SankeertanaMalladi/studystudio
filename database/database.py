import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

DATABASE_PATH = "database/users.db"


def create_database():
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS enrollments(
                user_id INTEGER NOT NULL,
                course_id TEXT NOT NULL,
                enrolled_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id, course_id),
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS quiz_results(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                course_id TEXT NOT NULL,
                mode TEXT NOT NULL,
                score INTEGER NOT NULL,
                total INTEGER NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)


def register_user(full_name, email, username, password):
    try:
        with sqlite3.connect(DATABASE_PATH) as connection:
            connection.execute(
                "INSERT INTO users (full_name,email,username,password) VALUES (?,?,?,?)",
                (full_name.strip(), email.strip().lower(), username.strip(), generate_password_hash(password)),
            )
        return True
    except sqlite3.IntegrityError:
        return False


def login_user(username, password):
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.row_factory = sqlite3.Row
        user = connection.execute(
            "SELECT id,full_name,email,username,password FROM users WHERE username=?",
            (username.strip(),),
        ).fetchone()
        if user is None:
            return None
        stored = user["password"]
        if stored.startswith(("scrypt:", "pbkdf2:")):
            valid = check_password_hash(stored, password)
        else:
            valid = stored == password
            if valid:
                connection.execute(
                    "UPDATE users SET password=? WHERE id=?",
                    (generate_password_hash(password), user["id"]),
                )
        if not valid:
            return None
        return {key: user[key] for key in ("id", "full_name", "email", "username")}


def get_enrollments(user_id):
    with sqlite3.connect(DATABASE_PATH) as connection:
        rows = connection.execute(
            "SELECT course_id FROM enrollments WHERE user_id=? ORDER BY enrolled_at DESC",
            (user_id,),
        ).fetchall()
    return [row[0] for row in rows]


def save_enrollments(user_id, course_ids):
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute("DELETE FROM enrollments WHERE user_id=?", (user_id,))
        for course_id in set(course_ids):
            connection.execute(
                "INSERT OR IGNORE INTO enrollments (user_id,course_id) VALUES (?,?)",
                (user_id, course_id),
            )


def record_quiz_result(user_id, course_id, mode, score, total):
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute(
            "INSERT INTO quiz_results (user_id,course_id,mode,score,total) VALUES (?,?,?,?,?)",
            (user_id, course_id, mode, score, total),
        )


def get_course_stats(user_id, course_id):
    with sqlite3.connect(DATABASE_PATH) as connection:
        row = connection.execute(
            "SELECT COUNT(*), ROUND(AVG(100.0*score/total)), MAX(created_at) "
            "FROM quiz_results WHERE user_id=? AND course_id=?",
            (user_id, course_id),
        ).fetchone()
    return {"attempts": row[0] or 0, "average": row[1], "last_attempt": row[2]}


def get_recent_results(user_id, limit=5):
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            "SELECT course_id,mode,score,total,created_at FROM quiz_results "
            "WHERE user_id=? ORDER BY id DESC LIMIT ?",
            (user_id, limit),
        ).fetchall()
    return [dict(row) for row in rows]
