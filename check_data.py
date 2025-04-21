import pandas as pd

# Read the dataset
df = pd.read_csv('medical_appointment.csv.csv')

# Display basic information
print("\nDataset Info:")
print("-" * 50)
print(f"Number of rows: {len(df)}")
print(f"Number of columns: {len(df.columns)}")
print("\nColumns:")
for col in df.columns:
    print(f"- {col}")

print("\nMissing values:")
print(df.isnull().sum())

print("\nFirst few rows:")
print(df.head()) 