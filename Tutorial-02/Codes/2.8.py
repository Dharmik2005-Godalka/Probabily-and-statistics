import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Tutorial 2  G1 A batch_MU_Students.xlsx")

for col in ['GPA','Salary','Spending','Text Messages']:
    plt.figure(figsize=(12,5))
    
    # histogram:
    plt.subplot(1,2,1)
    plt.hist(df[col], bins=10, edgecolor='black')
    plt.title(f'Histogram of {col}')
    
    plt.show()
    