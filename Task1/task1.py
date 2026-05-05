import pandas as pd
df = pd.read_csv("students.csv")
df.columns = df.columns.str.strip()  
df["AverageMarks"] = df[["Math","English","Science"]].mean(axis=1)
top_student = df.loc[df["AverageMarks"].idxmax()]
print(df)
print("\nTop Student:\n", top_student)
