import matplotlib.pyplot as plt
import seaborn as sns

# Example of a Bar Chart
sns.barplot(x='Category', y='Sales', data=df)
plt.title('Sales by Category')
plt.show()

# Example of a Line Chart
plt.plot(df['Date'], df['Revenue'])
plt.title('Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.show()
