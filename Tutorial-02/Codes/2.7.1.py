import pandas as pd

df = pd.read_excel("Tutorial 2  G1 A batch_MU_Students.xlsx")

total = len(df)

# count GPA < 3:
gpa_count = (df['GPA'] < 3).sum()
prob = gpa_count / total

print("Students with GPA < 3:", gpa_count)
print("Prob. GPA < 3:", round(prob, 4))
