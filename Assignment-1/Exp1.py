import numpy as np
import pandas as pd

# 1. NumPy Array Operations
marks = np.array([72, 85, 91, 68, 77, 88, 87, 75, 67, 88])

print("Marks:", marks)
print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))

# 2. Pandas DataFrame Creation
data = {
    "Name": ["Amit", "Riya", "Sourav", "Neha", "Rahul", "Aniket", "Raihan", "Praveen", "Nawed", "Ansh"],
    "Attendance": [88, 92, 76, 95, 81, 77, 87, 84, 76, 77],
    "Marks": [72, 85, 68, 91, 77, 88, 75, 76, 87, 74]
}

df = pd.DataFrame(data)

# 3. Data Exploration
print("\n--- First Ten Records ---")
print(df.head(10))

print("\n--- Data Information ---")
print(df.info())

print("\n--- Statistical Summary ---")
print(df.describe())

print("\nAverage Marks:", df["Marks"].mean())