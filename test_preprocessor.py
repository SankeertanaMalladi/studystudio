from utils.preprocessor import preprocess_input

student = {

    "Gender":"Female",

    "Department":"Computer Science",

    "Extracurricular_Activities":"Yes",

    "Internet_Access_at_Home":"Yes",

    "Parent_Education_Level":"Bachelor",

    "Family_Income_Level":"Medium"

}

df = preprocess_input(student)

print(df)