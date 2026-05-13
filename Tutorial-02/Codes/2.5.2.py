import pandas as pd

df = pd.read_excel("Tutorial 2  G1 A batch_MU_Students.xlsx")

total = len(df)

female_df = df[df['Gender'] == 'Female']
total = len(female_df)

female_ib_count = ((female_df['Major'] == 'International Business') | 
                        (female_df['Major'] == 'Management')).sum()

conditional = female_ib_count / total

print("female total:", total)
print("female in IB or manag.:", female_ib_count)
print("Cond. prob.:", round(conditional, 4))
