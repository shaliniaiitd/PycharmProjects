import pandas as pd

df = pd.read_excel('/content/Sample - Superstore.xls')
df.head(10)
df.tail(10)
df.groupby("State")["Sales"].sum()
#df.groupby("Category")["Sales"].describe()
df.groupby("Category")["Profit"].describe()
# .mean()
# .median()
# .describe()

#plt.figure(figsize()
import seaborn as sbn

# sbn.boxplot(x='Sales',y='Category',data=df.sample(100))
# sbn.catplot(data=df,kind='bar', x='Category' , y='Sales')
sbn.scatterplot(x="Sales",y='Profit',data=df, hue='Sub-Category', sizes = (1,8))
#Used to point out outliers
#Top 10 states in decreasing order of mean profit
#df.groupby("State")["Profit"].mean().sort_values(ascending=False).head(10)
#Top 10 states in increasing order of mean profit
df.groupby("State")["Profit"].mean().sort_values(ascending=True).head(10)