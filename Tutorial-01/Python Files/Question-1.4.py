import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("Wholesale_customers_data.xlsx")

# Boxplot:
plt.figure(figsize=(10,6))

sns.boxplot(data=df[["Fresh","Milk","Grocery","Frozen","Detergents_Paper","Delicassen"]])
plt.title("Outlier Detection in Item Spending")
plt.ylabel("Spending Amount")
plt.xticks(rotation=45)
plt.show()

# Outlier:
outlier = {}
for col in ["Fresh","Milk","Grocery","Frozen","Detergents_Paper","Delicassen"]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
    outlier[col] = {
        "Lower Bound": lower_bound,
        "Upper Bound": upper_bound,
        "Number of Outliers": outliers.count()
    }

for item, values in outlier.items():
    print(f"{item}:")
    print(f"  Lower Bound: {values['Lower Bound']}")
    print(f"  Upper Bound: {values['Upper Bound']}")
    print(f"  Number of Outliers: {values['Number of Outliers']}\n")