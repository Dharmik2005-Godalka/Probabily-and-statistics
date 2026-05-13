import pandas as pd

df = pd.read_excel("Tutorial 2  G1 A batch_MU_Students.xlsx")

# filtering undecided
grad = df[df['Grad Intention'].isin(['Yes','No'])]

# contingency table: 
table_grad = pd.crosstab(grad['Gender'], grad['Grad Intention'])
print(table_grad)

# independence check
total = len(grad)
prob_female = (grad['Gender'] == 'Female').sum() / total
prob_yes = (grad['Grad Intention'] == 'Yes').sum() / total
female_and_yes = ((grad['Gender'] == 'Female') & (grad['Grad Intention'] == 'Yes')).sum() / total

print("P(Female):", round(prob_female,4))
print("P(Yes):", round(prob_yes,4))
print("P(Female AND Yes):", round(female_and_yes,4))
print("P(Female)*P(Yes):", round(prob_female*prob_yes,4))
