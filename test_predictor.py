from utils.predictor import predict_grade

student = {

    "Gender": "Female",
    "Age": 22,
    "Department": "Computer Science",

    "Attendance (%)": 82,
    "Midterm_Score": 78,
    "Final_Score": 81,
    "Assignments_Avg": 80,
    "Quizzes_Avg": 70,
    "Participation_Score": 8,
    "Projects_Score": 84,

    "Study_Hours_per_Week": 12,

    "Extracurricular_Activities": "Yes",
    "Internet_Access_at_Home": "Yes",

    "Parent_Education_Level": "Bachelor",

    "Family_Income_Level": "Medium",

    "Stress_Level (1-10)": 5,

    "Sleep_Hours_per_Night": 7

}

grade = predict_grade(student)

print("=" * 40)
print("Predicted Grade")
print("=" * 40)

print(grade)