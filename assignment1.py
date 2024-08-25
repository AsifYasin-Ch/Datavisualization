import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r'C:\study\IT8104\Assignment 1\black-friday_prediction\your_dataset.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
print(df.head())

# 1. Histogram of Purchases
plt.figure(figsize=(10, 6))
plt.hist(df['Purchase'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Purchases')
plt.xlabel('Purchase Amount')
plt.ylabel('Frequency')
plt.show()

# 2. Bar Chart of Average Purchase by City Category
avg_purchase_city = df.groupby('City_Category')['Purchase'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='City_Category', y='Purchase', data=avg_purchase_city, palette='viridis')
plt.title('Average Purchase by City Category')
plt.xlabel('City Category')
plt.ylabel('Average Purchase')
plt.show()

# 3. Pie Chart of Purchase Distribution by Gender
purchase_gender = df.groupby('Gender')['Purchase'].sum().reset_index()
plt.figure(figsize=(8, 8))
plt.pie(purchase_gender['Purchase'], labels=purchase_gender['Gender'], autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'])
plt.title('Purchase Distribution by Gender')
plt.show()

# 4. Box Plot of Purchase by Age Group
plt.figure(figsize=(12, 6))
sns.boxplot(x='Age', y='Purchase', data=df, palette='Set2')
plt.title('Box Plot of Purchase by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Purchase Amount')
plt.show()
