import pandas as pd
df=pd.read_csv('data.csv')
print("Mean:", df["Marks"].mean())
print("Median:", df["Marks"].median())
print("Min:", df["Marks"].min())
print("Max:", df["Marks"].max())
print("Std:", df["Marks"].std())
print(df.describe())
