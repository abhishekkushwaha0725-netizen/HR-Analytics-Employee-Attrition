import pandas as pd
import matplotlib.pyplot as plt

# 1. Data Load
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
print("Total Employees:", df.shape[0])

# 2. Graph 1: Attrition by Age Group
plt.figure(figsize=(10,6))
attrition_age = pd.crosstab(df['Age'], df['Attrition'])
attrition_age['Yes'].plot(kind='bar', color='crimson')
plt.title('Employee Attrition by Age Group', fontsize=16, fontweight='bold')
plt.xlabel('Age')
plt.ylabel('Employees Who Left Company')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('attrition_by_age.png')
print("Graph 1 Saved: attrition_by_age.png")

# 3. Graph 2: Department-wise Attrition Rate %
dept_attrition = df.groupby('Department')['Attrition'].value_counts(normalize=True).unstack() * 100
dept_attrition = dept_attrition['Yes'].sort_values(ascending=False)

plt.figure(figsize=(8,8))
dept_attrition.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff6b6b','#4ecdc4','#45b7d1'])
plt.title('Attrition Rate % by Department', fontsize=16, fontweight='bold')
plt.ylabel('')
plt.tight_layout()
plt.savefig('attrition_by_department.png')
print("Graph 2 Saved: attrition_by_department.png")

# 4. Bonus Insight: Salary vs Attrition
salary_impact = df.groupby('Attrition')['MonthlyIncome'].mean()
print("\nAvg Monthly Income:")
print("Employees who Stayed: ₹", int(salary_impact['No']))
print("Employees who Left: ₹", int(salary_impact['Yes']))