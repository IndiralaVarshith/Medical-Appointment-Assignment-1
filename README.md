# Medical Appointment Data Cleaning

This project cleans and prepares the Medical Appointment No Shows dataset from Kaggle.

## Setup

1. Download the dataset:
   - Go to Kaggle and search for "Medical Appointment No Shows"
   - Download the dataset and rename it to `medical_appointment.csv`
   - Place the file in the same directory as the scripts

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the cleaning script:
   ```bash
   python data_cleaning.py
   ```

## What the Script Does

The script performs the following cleaning operations:

1. Handles missing values:
   - Numeric columns: filled with median
   - Categorical columns: filled with mode

2. Removes duplicate rows

3. Standardizes data:
   - Converts date columns to datetime format
   - Standardizes categorical variables (e.g., gender to lowercase)
   - Renames columns to be clean and uniform (lowercase, underscores)

4. Fixes data types:
   - Converts appropriate numeric columns to categorical
   - Ensures dates are in datetime format

## Output

The script generates two files:

1. `cleaned_medical_appointment.csv`: The cleaned dataset
2. `cleaning_summary.txt`: A summary of all changes made during cleaning

## Data Dictionary

After cleaning, the dataset will have standardized column names. Common columns include:
- patient_id
- appointment_id
- gender
- scheduled_day
- appointment_day
- age
- neighbourhood
- scholarship
- hypertension
- diabetes
- alcoholism
- handicap
- sms_received
- no_show

Note: Actual columns may vary depending on the version of the dataset. 