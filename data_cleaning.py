import pandas as pd
import numpy as np
from datetime import datetime

def clean_medical_appointment_data():
    # Load the dataset
    print("Loading dataset...")
    df = pd.read_csv('medical_appointment.csv.csv')
    
    # Store original shape
    original_shape = df.shape
    
    # Clean column names (convert to lowercase and replace spaces/special characters with underscores)
    print("\nCleaning column names...")
    df.columns = df.columns.str.lower().str.replace('-', '_').str.replace(' ', '_')
    
    # Convert date columns to datetime
    print("\nConverting date columns...")
    df['scheduledday'] = pd.to_datetime(df['scheduledday'])
    df['appointmentday'] = pd.to_datetime(df['appointmentday'])
    
    # Fix data types
    print("\nFixing data types...")
    # Convert age to integer
    df['age'] = df['age'].astype(int)
    
    # Convert binary columns to proper boolean/integer
    binary_columns = ['scholarship', 'hipertension', 'diabetes', 'alcoholism', 'sms_received']
    for col in binary_columns:
        df[col] = df[col].astype(int)
    
    # Standardize gender values
    df['gender'] = df['gender'].str.lower()
    
    # Convert no_show to boolean (1 for Yes, 0 for No)
    df['no_show'] = (df['no_show'] == 'Yes').astype(int)
    
    # Handle any missing values
    print("\nHandling missing values...")
    print("Missing values before cleaning:")
    print(df.isnull().sum())
    
    # Fill missing values appropriately
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())
    
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    # Remove duplicates
    print("\nRemoving duplicates...")
    initial_rows = len(df)
    df = df.drop_duplicates()
    removed_rows = initial_rows - len(df)
    print(f"Removed {removed_rows} duplicate rows")
    
    # Add derived features
    print("\nAdding derived features...")
    # Calculate days until appointment
    df['days_until_appointment'] = (df['appointmentday'] - df['scheduledday']).dt.days
    
    # Generate summary
    print("\nCleaning Summary:")
    print("-" * 50)
    print(f"Original shape: {original_shape}")
    print(f"Final shape: {df.shape}")
    print(f"Duplicates removed: {removed_rows}")
    print("\nColumns in cleaned dataset:")
    for col in df.columns:
        print(f"- {col}: {df[col].dtype}")
    
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())
    
    # Save cleaned dataset
    print("\nSaving cleaned dataset...")
    df.to_csv('cleaned_medical_appointment.csv', index=False)
    print("Cleaned dataset saved as 'cleaned_medical_appointment.csv'")
    
    return df

if __name__ == "__main__":
    cleaned_df = clean_medical_appointment_data() 