import pandas as pd

#load excel fiile
df = pd.read_excel("BlinkIT Grocery Data.xlsx")

#check null values

print("Null values:\n", df.isnull().sum())

#Fill missing values (median)

df.fillna(df.median(numeric_only=True), inplace=True)

# Save cleaned file

df.to_excel("cleaned_output.xlsx", index=False)

print("Done bro ✅ File cleaned and saved")
