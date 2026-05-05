import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('UserRate.csv')
plt.bar(df['User'],df['Satisfaction'])
plt.xlabel("User")
plt.ylabel("Satisfaction")
plt.title("User Satisfaction Rate")
plt.show()
