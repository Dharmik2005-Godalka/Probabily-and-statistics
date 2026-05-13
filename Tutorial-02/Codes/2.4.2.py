import pandas as pd

df = pd.read_excel("Tutorial 2  G1 A batch_MU_Students.xlsx")

# female and does not have a laptop
female_count = ((df['Gender'] == 'Female') & (df['Computer'] != 'Laptop')).sum()
total = len(df)

prob = female_count / total

print("Female & no laptop count:", female_count)
print("Prob.:", round(prob, 4))