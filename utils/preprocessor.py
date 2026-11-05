import pandas as pd
import joblib

# Load encoders
encoders = joblib.load("models/label_encoders.pkl")


def calculate_learning_speed(student):
    """
    Automatically calculate learning speed.
    """

    study_hours = student["Study_Hours_per_Week"]
    quiz = student["Quizzes_Avg"]
    attendance = student["Attendance (%)"]

    if study_hours >= 15 and quiz >= 80 and attendance >= 85:
        return "Fast"

    elif study_hours >= 10 and quiz >= 60:
        return "Medium"

    else:
        return "Slow"


def preprocess_input(student):

    # Calculate Learning Speed automatically
    student["Learning_Speed"] = calculate_learning_speed(student)

    df = pd.DataFrame([student])

    categorical_columns = [

        "Gender",
        "Department",
        "Extracurricular_Activities",
        "Internet_Access_at_Home",
        "Parent_Education_Level",
        "Family_Income_Level",
        "Learning_Speed"

    ]

    for column in categorical_columns:

        if column in df.columns:

            encoder = encoders[column]

            encoded_values = []

            for value in df[column]:

                if value in encoder.classes_:

                    encoded_values.append(
                        encoder.transform([value])[0]
                    )

                else:

                    print(
                        f"Warning : Unknown value '{value}' in {column}"
                    )

                    encoded_values.append(0)

            df[column] = encoded_values

    return df