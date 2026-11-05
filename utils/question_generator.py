import pandas as pd

# Load dataset
questions = pd.read_csv("data/questions_dataset.csv")


def get_questions(subject, num_questions=5):

    subject_questions = questions[
        questions["Subject"] == subject
    ]

    subject_questions = subject_questions.sample(
        n=min(num_questions, len(subject_questions))
    )

    return subject_questions.reset_index(drop=True)