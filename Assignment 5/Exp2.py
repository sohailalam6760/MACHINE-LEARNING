import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score

data = {
    "StudyHours": [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 9],
    "Attendance": [55, 60, 65, 70, 72, 75, 78, 80, 85, 88, 92, 95],
    "Pass": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["StudyHours", "Attendance"]]
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

y_prob = model.predict_proba(X_test)[:, 1]

thresholds = [0.3, 0.5, 0.7]

print("--- Threshold Comparison ---")

for threshold in thresholds:

    y_pred = (y_prob >= threshold).astype(int)

    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)

    print("\nThreshold:", threshold)
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))