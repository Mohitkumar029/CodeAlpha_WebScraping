import pandas as pd

df = pd.read_csv("books_raw.csv")

# 1. Check the data first
print(df.info())
print("Missing values:")
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# 2. Price: remove the pound sign and make it a number
df["Price"] = df["Price"].str.replace("£", "", regex=False).astype(float)

# 3. Rating: change words to numbers
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["Rating"] = df["Rating"].map(rating_map)

# 4. Check the result and save
print(df.dtypes)
print(df.describe())
df.to_csv("books_clean.csv", index=False)
print("Clean file saved")