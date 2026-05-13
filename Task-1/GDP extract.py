import pandas as pd

# Load original file
file_path = "Components of Gross Domestic Product (1).xlsx"

# Read full sheet first
df = pd.read_excel(file_path, header=None)

# 🔍 Step 1: Find where "2011-2012" table starts
start_row = None
for i in range(len(df)):
    if df.iloc[i].astype(str).str.contains("2011-2012").any():
        start_row = i
        break

# Read again from that point
df = pd.read_excel(file_path, skiprows=start_row)

# 🔍 Step 2: Clean headers (take first row as header)
df.columns = df.iloc[0]
df = df[1:]

# 🔍 Step 3: Keep only required columns
# (You may need to adjust column names slightly after printing them)
print(df.columns)  # check names once

# Example selection (adjust if names differ)
df = df[["Year", "GDP at Constant Prices", "GDP at Current Prices"]]

# 🔍 Step 4: Clean data
df = df.dropna()
df["Year"] = df["Year"].astype(int)

# 🔍 Step 5: Save new Excel file
df.to_excel("Clean_GDP_2011_2012.xlsx", index=False)

print("✅ New file created: Clean_GDP_2011_2012.xlsx")