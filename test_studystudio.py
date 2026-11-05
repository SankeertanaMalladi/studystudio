from utils.report_generator import generate_report

student = {

    "Gender":"Female",
    "Age":22,
    "Department":"Computer Science",

    "Attendance (%)":82,
    "Midterm_Score":78,
    "Final_Score":81,
    "Assignments_Avg":80,
    "Quizzes_Avg":70,
    "Participation_Score":8,
    "Projects_Score":84,

    "Study_Hours_per_Week":12,

    "Extracurricular_Activities":"Yes",

    "Internet_Access_at_Home":"Yes",

    "Parent_Education_Level":"Bachelor",

    "Family_Income_Level":"Medium",

    "Stress_Level (1-10)":5,

    "Sleep_Hours_per_Night":7

}

subject = "Python"

report = generate_report(
    student,
    subject
)

print("="*60)
print("STUDYSTUDIO REPORT")
print("="*60)

print("\nPredicted Grade")
print(report["predicted_grade"])

print("\nSubject")
print(report["subject"])

print("\nRecommendations")

for item in report["recommendations"]:
    print("-", item)

print("\nStudy Materials")

print(
    report["study_materials"][
        ["Resource_Name","Topic","Difficulty"]
    ]
)

print("\nPractice Questions")

for index,row in report["practice_questions"].iterrows():

    print("-"*40)

    print(row["Question"])

print("\nFeedback")

for item in report["feedback"]:

    print("-",item)

print("\nWeekly Study Plan")

for day,task in report["study_plan"].items():

    print(day,":",task)

print("\nSuggestions")

for item in report["suggestions"]:

    print("-",item)
