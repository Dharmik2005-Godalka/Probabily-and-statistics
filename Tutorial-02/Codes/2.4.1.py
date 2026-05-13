import pandas as pd

df = pd.read_excel("Tutorial 2  G1 A batch_MU_Students.xlsx")

# male and intends to graduate:
male_g_count = ((df['Gender'] == 'Male') & (df['Grad Intention'] == 'Yes')).sum()
total = len(df)

prob_male = male_g_count / total

print("Male & intends to graduate count:", male_g_count)
print("Prob.:", round(prob_male, 4))
