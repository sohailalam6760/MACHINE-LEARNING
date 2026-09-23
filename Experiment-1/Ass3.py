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

def assign_grade(marks):
    if marks >= 90:
        return 'A'
    elif 80 <= marks <= 89:
        return 'B'
    elif 70 <= marks <= 79:
        return 'C'
    elif 60 <= marks <= 69:
        return 'D'
    else:
        return 'Fail'

# Add Grade column
df["Grade"] = df["Marks"].apply(assign_grade)

print(df)