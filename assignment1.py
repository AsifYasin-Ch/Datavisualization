import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Correct file path
file_path = r'C:\study\IT8104\Assignment 1\black-friday_prediction\test.csv'
df = pd.read_csv(file_path)

# Print column names to confirm the structure
print(df.columns)

# 1. Histogram of Product Category 1
plt.figure(figsize=(10, 6))
plt.hist(df['Product_Category_1'].dropna(), bins=range(int(df['Product_Category_1'].max())+1), color='skyblue', edgecolor='black')
plt.title('Histogram of Product Category 1')
plt.xlabel('Product Category 1')
plt.ylabel('Frequency')
plt.show()

# 2. Bar Chart of Average Product Category 1 by City Category
avg_category_city = df.groupby('City_Category')['Product_Category_1'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='City_Category', y='Product_Category_1', data=avg_category_city, palette='viridis')
plt.title('Average Product Category 1 by City Category')
plt.xlabel('City Category')
plt.ylabel('Average Product Category 1')
plt.show()

# 3. Pie Chart of Gender Distribution
gender_distribution = df['Gender'].value_counts().reset_index()
gender_distribution.columns = ['Gender', 'Count']
plt.figure(figsize=(8, 8))
plt.pie(gender_distribution['Count'], labels=gender_distribution['Gender'], autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'])
plt.title('Gender Distribution')
plt.show()

# 4. Count Plot of Product Categories by Age Group
plt.figure(figsize=(12, 6))
sns.countplot(x='Age', hue='Product_Category_1', data=df, palette='Set2')
plt.title('Count of Product Category 1 by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()
