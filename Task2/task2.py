import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sales.csv')
plt.plot(df['Month'], df['Sales'])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Trend")
plt.show()
