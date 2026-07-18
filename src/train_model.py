import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("../data/student_performance_encoded.csv")

# Features
X = df[
    [
        "AttendanceRate",
        "StudyHoursPerWeek",
        "PreviousGrade",
        "ExtracurricularActivities"
    ]
]

# Target
y = df["FinalGrade"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained successfully!")
print("model.pkl created.")
