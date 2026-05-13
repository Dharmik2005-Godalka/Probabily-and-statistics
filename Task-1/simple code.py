import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("Orginal Data.xlsx")

# Extract variables
X = df["POPULATION"]
Y = df["Gross Domestic Product"]

# scaleing data:
X = X / 1e9      # population in billions
Y = Y / 1e12     # GDP in trillions

n = len(X)

# Least Squares calculation:
sum_x = X.sum()
sum_y = Y.sum()
sum_xy = (X * Y).sum()
sum_x2 = (X * X).sum()

# Slope, Intercept:
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - (sum_x ** 2))
c = (sum_y - m * sum_x) / n

print("Slope (m):", m)
print("Intercept (c):", c)

# predicted value:
pred = m * X + c

# sort values:
sorted_indices = X.argsort()
sort1 = X.iloc[sorted_indices]
pred_sorted = pred.iloc[sorted_indices]

# graph:
plt.figure(figsize=(8,5))

plt.scatter(X, Y, label="Actual Data")
plt.plot(sort1, pred_sorted, color='red', label="Regression Line")

plt.xlabel("Population (billions)")
plt.ylabel("GDP (trillions)")
plt.title("GDP vs Population")

plt.legend()
plt.grid()

plt.show()