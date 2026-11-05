import pandas as pd

# Load study materials dataset
materials = pd.read_csv("data/study_materials_dataset.csv")


def get_difficulty(grade):
    """
    Convert predicted grade to study material difficulty.
    """

    if grade == "A":
        return "Hard"

    elif grade in ["B", "C"]:
        return "Medium"

    else:
        return "Easy"


def recommend_material(student, subject, predicted_grade):

    recommendations = []

    # ------------------------------------
    # Student Performance Recommendations
    # ------------------------------------

    if student["Attendance (%)"] < 75:
        recommendations.append(
            "Improve attendance by attending lectures regularly."
        )

    if student["Quizzes_Avg"] < 60:
        recommendations.append(
            "Practice previous quiz papers."
        )

    if student["Assignments_Avg"] < 70:
        recommendations.append(
            "Complete additional assignments."
        )

    if student["Midterm_Score"] < 60:
        recommendations.append(
            "Revise classroom notes before attempting advanced topics."
        )

    if student["Study_Hours_per_Week"] < 10:
        recommendations.append(
            "Increase study time to at least 12 hours per week."
        )

    if student["Stress_Level (1-10)"] >= 8:
        recommendations.append(
            "Take short breaks and manage stress."
        )

    if student["Sleep_Hours_per_Night"] < 6:
        recommendations.append(
            "Sleep at least 7 hours every night."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Excellent performance! Keep up your current routine."
        )

    # ------------------------------------
    # Dataset-Based Study Materials
    # ------------------------------------

    difficulty = get_difficulty(predicted_grade)

    study_materials = materials[
        (materials["Subject"] == subject) &
        (materials["Difficulty"] == difficulty)
    ]

    if study_materials.empty:
        study_materials = materials[
            materials["Subject"] == subject
        ]

    study_materials = study_materials.head(5)

    return recommendations, study_materials