import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# ==============================
# LOAD CLEAN DATASET
# ==============================

df = pd.read_csv("dataset/clean_student_data.csv")

print("Dataset Loaded Successfully")

print(df.head())

# ==============================
# LABEL ENCODING
# ==============================

label_encoders = {}

categorical_columns = df.select_dtypes(include=["object", "string"]).columns

for column in categorical_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(df[column])

    label_encoders[column] = encoder

print("\nCategorical Columns Encoded Successfully")

# ==============================
# FEATURES AND TARGET
# ==============================

X = df.drop("Grade", axis=1)

y = df["Grade"]

print("\nFeatures Shape :", X.shape)

print("Target Shape :", y.shape)

# ==============================
# TRAIN TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Data :", X_train.shape)
print("Testing Data :", X_test.shape)

# ==============================
# TRAIN MODEL
# ==============================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel Training Completed")

# ==============================
# PREDICTIONS
# ==============================

predictions = model.predict(X_test)

# ==============================
# MODEL EVALUATION
# ==============================

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy")

print(accuracy)

print("\nClassification Report")

print(classification_report(y_test, predictions))

# ==============================
# SAVE MODEL
# ==============================

joblib.dump(
    model,
    "models/studystudio_model.pkl"
)

joblib.dump(
    label_encoders,
    "models/label_encoders.pkl"
)

joblib.dump(
    list(X.columns),
    "models/feature_columns.pkl"
)

print("\nModel Saved Successfully")