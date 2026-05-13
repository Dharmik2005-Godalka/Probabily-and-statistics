import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("Wholesale_customers_data.xlsx")

# Boxplot:
plt.figure(figsize=(10,6))
sns.boxplot(data=df[["Fresh","Milk","Grocery","Frozen","Detergents_Paper","Delicassen"]])
plt.title("Item Distribution and Variability")
plt.ylabel("Spending Amount")

plt.xticks(rotation=45)
plt.show()

# Standard dev:
std = df[["Fresh","Milk","Grocery","Frozen","Detergents_Paper","Delicassen"]].std()
print("Standard Deviation of each Type:\n", std)
