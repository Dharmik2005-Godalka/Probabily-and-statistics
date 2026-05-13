import pandas as pd

#load file for next cal.
df = pd.read_excel("Tutorial 2  G1 A batch_MU_Students.xlsx")

# Total:
total = len(df)

# Count both (1-male) and (2-Female):
count1 = (df['Gender'] == 'Male').sum()
count2 = (df['Gender'] == 'Female').sum()

# prob.
p_male = count1 / total
p_female = count2 / total

# result:
print("Total students:", total)
print("Male count:", count1, "Probability Male:", round(p_male, 4))
print("Female count:", count2, "Probability Female:", round(p_female, 4))