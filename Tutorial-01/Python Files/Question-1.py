import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Wholesale_customers_data.xlsx")

# Basic info abot this:
print(df.info())
print(df.describe())
