import pandas as pd

# Sample data for clearance
data = {
    'Student_ID': ['S101', 'S102', 'S103'],
    'Name': ['Aman', 'Riya', 'Kunal'],
    'Library_Clearance': ['Yes', 'No', 'Yes'],
    'Lab_Clearance': ['Yes', 'Yes', 'No'],
    'Hostel_Clearance': ['No', 'Yes', 'Yes'],
    'Accounts_Clearance': ['Yes', 'Yes', 'Yes']
}

# Create DataFrame
df = pd.DataFrame(data)

# Check who is fully cleared
df['Fully_Cleared'] = df[['Library_Clearance', 'Lab_Clearance', 'Hostel_Clearance', 'Accounts_Clearance']].apply(
    lambda row: 'Yes' if all(cell == 'Yes' for cell in row) else 'No', axis=1
)

# Save to CSV
df.to_csv('student_clearance.csv', index=False)

print("CSV file 'student_clearance.csv' created successfully.")
