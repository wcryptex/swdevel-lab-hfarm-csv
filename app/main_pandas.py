import pandas as pd

# Step 2: Read CSV file into a DataFrame
df = pd.read_csv('employees.csv')

# Step 3: Explore and manipulate the data
print("DataFrame:")
print(df)

# Access specific columns
print("\nAge column:")
print(df['Age'])

# Filter data
print("\nEmployees in Engineering department:")
print(df[df['Department'] == 'Engineering'])

# Group by and calculate average salary per department
print("\nAverage salary per department:")
average_salary = df.groupby('Department')['Salary'].mean()
print(average_salary)
