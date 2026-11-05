from utils.recommendation import recommend_material

student = {

    "Attendance (%)":82,
    "Quizzes_Avg":70,
    "Assignments_Avg":80,
    "Midterm_Score":78,
    "Study_Hours_per_Week":12,
    "Stress_Level (1-10)":5,
    "Sleep_Hours_per_Night":7

}

recommendations, materials = recommend_material(
    student,
    "Python",
    "C"
)

print("Recommendations")
for item in recommendations:
    print("-", item)

print("\nStudy Materials")
print(materials[["Resource_Name", "Topic", "Difficulty"]])