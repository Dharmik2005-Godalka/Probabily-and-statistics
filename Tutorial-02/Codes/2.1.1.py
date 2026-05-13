import pandas as pd

# Load file for checking:
df = pd.read_excel("Tutorial 2  G1 A batch_MU_Students.xlsx")

table1 = pd.crosstab(df['Gender'], df['Major'])
print(table1)
