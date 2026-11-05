from utils.feedback import generate_feedback

student = {

    "Attendance (%)":70,
    "Quizzes_Avg":55,
    "Assignments_Avg":65,
    "Study_Hours_per_Week":8,
    "Stress_Level (1-10)":9,
    "Sleep_Hours_per_Night":5

}

feedback = generate_feedback(
    student,
    "C"
)

print("=" * 50)
print("PERSONALIZED FEEDBACK")
print("=" * 50)

for item in feedback:
    print("•", item)