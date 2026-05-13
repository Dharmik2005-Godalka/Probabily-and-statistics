import pandas as pd

#load file for next cal.
df = pd.read_excel("Tutorial 2  G1 A batch_MU_Students.xlsx")

# Separate male and female:
male_df = df[df['Gender'] == 'Male']
female_df = df[df['Gender'] == 'Female']

# Cond. prob. of major:
c_p_male = male_df['Major'].value_counts(normalize=True)
c_p_female = female_df['Major'].value_counts(normalize=True)

print("Cond. Prob. of Major among Male Students:\n", c_p_male)
print("\nCond. Prob. of Major among Female Students:\n", c_p_female)
