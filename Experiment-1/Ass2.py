import numpy as np
import pandas as pd

marks = np.array([72, 85, 91, 68, 77, 88, 87, 75, 67, 88])

print("Marks:", marks)
print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))

data = {
    "Name": ["Amit", "Riya", "Sourav", "Neha", "Rahul", "Aniket", "Raihan", "Praveen", "Nawed", "Ansh"],
    "Roll no.": [10, 15, 16, 20, 12, 18, 22, 24, 36, 44],
    "Attendance": [88, 92, 76, 95, 81, 77, 87, 84, 76, 77],
    "Marks": [72, 85, 68, 91, 77, 88, 75, 76, 87, 74]
}

df = pd.DataFrame(data)

print("\n--- First Ten Records ---")
print(df.head(10))

print("\n--- Data Information ---")
print(df[df["Marks"]>80])

print("\n--- Statistical Summary ---")
print(df.describe())

print("\nAverage Marks:", df["Marks"].mean())