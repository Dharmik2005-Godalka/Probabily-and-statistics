import pandas as pd

# Load file for checking:
df = pd.read_excel("Tutorial 2  G1 A batch_MU_Students.xlsx")

table4 = pd.crosstab(df['Gender'], df['Computer'])
print(table4)
