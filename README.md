# StudyStudio

StudyStudio is a Flask learning platform where students choose courses that interest them and practice with flashcards, quizzes, mock tests, curated learning resources, and a personalized study coach.

## Features

- Student registration and sign-in, with passwords stored as hashes
- Sixteen course tracks: Python, JavaScript, Web Development, Java, SQL, Data Science, Machine Learning, Data Structures & Algorithms, React, C++, Git & GitHub, Cybersecurity, Cloud Computing, Statistics & Probability, UI & UX Design, and Excel for Data Analysis
- Course selection and a dashboard with saved quiz history and score summaries
- Original flashcards and multiple-choice questions for each course
- Practice quizzes and mock assessments, with answer explanations after submission
- Curated documentation, learning paths, interactive practice, and video lesson links
- A study coach that builds a weekly plan from a student’s course, goal, available time, and latest quiz score
- Light and dark themes, with the chosen theme remembered in the browser

The study coach uses the student’s progress and preferences with built-in rules. The app does not call an external generative AI service.

## Run locally in VS Code

Open this folder in VS Code. In the integrated terminal, run:

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
    python app.py

If the py launcher is not installed, use python instead:

    python -m venv .venv

Then open http://127.0.0.1:5000, create an account, and choose courses from the course library. Keep the terminal running while using the app. Press Ctrl+C in that terminal to stop it.

If PowerShell prevents environment activation, run the environment’s Python directly:

    .\.venv\Scripts\python.exe -m pip install -r requirements.txt
    .\.venv\Scripts\python.exe app.py

Run python app.py from the project root so the SQLite database is created under database.

## Project structure

    studystudio/
    ├── app.py                 Flask routes and learning flows
    ├── course_content.py      Course catalog, flashcards, questions, and resources
    ├── database/
    │   └── database.py        Accounts, enrollments, and quiz history
    ├── static/
    │   ├── css/style.css      Responsive light and dark themes
    │   └── js/theme.js        Saved theme preference
    ├── templates/             Flask/Jinja pages
    ├── requirements.txt
    └── README.md

The older datasets and model files are retained locally for the earlier prototype. The current course experience uses course_content.py; the legacy files are not needed to run the app and are excluded from Git by default.

## Publish to GitHub

1. In VS Code, open Source Control with Ctrl+Shift+G and choose Initialize Repository.
2. Review the files Git lists. The .gitignore excludes the local account database, virtual environments, legacy CSV datasets, and saved model binaries.
3. Stage the source files, enter a commit message, and select Commit.
4. Open the Command Palette with Ctrl+Shift+P, run Publish to GitHub, sign in, and choose a repository name and visibility.

Before publishing, review the staged changes and make sure they contain no private student data, credentials, or other files you do not intend to share.

## Notes

- The Flask development server is for local development. Use a production WSGI server and a securely configured secret key before deploying publicly.
- Student accounts, course selections, and quiz results are stored in the local SQLite database. That database is excluded from Git.
- Some learning and video links open external websites.
