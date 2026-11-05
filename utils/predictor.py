import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/student_performance_model.pkl")

# Load label encoders
encoders = joblib.load("models/label_encoders.pkl")


def predict_performance(subject,
                        quiz_score,
                        level,
                        learning_style):

    data = pd.DataFrame({

        "Subject": [subject],

        "Quiz_Score": [quiz_score],

        "Skill_Level": [level],

        "Learning_Style": [learning_style]

    })

    # Encode categorical columns

    for column in ["Subject",
                   "Skill_Level",
                   "Learning_Style"]:

        data[column] = encoders[column].transform(
            data[column]
        )

    prediction = model.predict(data)[0]

    return prediction