import pandas as pd

df = pd.read_excel("Tutorial 2  G1 A batch_MU_Students.xlsx")

total = len(df)

# count:
male_count = (df['Gender'] == 'Male').sum()
fulltime_count = (df['Employment'] == 'Full-Time').sum()
male_fulltime_count = ((df['Gender'] == 'Male') & (df['Employment'] == 'Full-Time')).sum()

# prob.
prob = (male_count + fulltime_count - male_fulltime_count) / total

print("male count:", male_count)
print("full-time count:", fulltime_count)
print("male & full-time count:", male_fulltime_count)
print("prob.:", round(prob, 4))
