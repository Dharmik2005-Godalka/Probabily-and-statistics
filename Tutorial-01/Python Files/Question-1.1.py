import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Wholesale_customers_data.xlsx")

# Channel-wise:
channel = df.groupby("Channel")[["Fresh","Milk","Grocery","Frozen","Detergents_Paper","Delicassen"]].mean()
channel.plot(kind="bar")

plt.title("Channel-wise Average Spending")
plt.ylabel("Amount")
plt.xticks(rotation=0)

plt.show()

# Reigon-wise:
region = df.groupby("Region")[["Fresh","Milk","Grocery","Frozen","Detergents_Paper","Delicassen"]].mean()
region.plot(kind="bar")

plt.title("Region-wise Average Spending")
plt.ylabel("Amount")
plt.xticks(rotation=0)

plt.show()

print("Region-wise mean:\n", region)
print("\nChannel-wise mean:\n", channel)