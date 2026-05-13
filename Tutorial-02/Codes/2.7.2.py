import pandas as pd

df = pd.read_excel("Tutorial 2  G1 A batch_MU_Students.xlsx")

male = df[df['Gender'] == 'Male']
female = df[df['Gender'] == 'Female']

# male cond. prob:
male_salary_count = (male['Salary'] >= 50).sum()
prob1 = male_salary_count / len(male)

# Female cond. prob:
female_salary_count = (female['Salary'] >= 50).sum()
prob2 = female_salary_count / len(female)

print("Male Salary >= 50:", male_salary_count, "Probability:", round(prob1,4))
print("Female Salary >= 50:", female_salary_count, "Probability:", round(prob2,4))

