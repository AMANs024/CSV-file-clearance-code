

# Project1 (To calculate the highest marks avg marks and pass fail status of students)
# Input: CSV file with student names and marks
# Task: Calculate average, highest scorer, and pass/fail status/

import pandas as pd
df = pd.read_csv('student.csv')
print(df.head())
print(df)
df['Pass'] = df['Marks'] >= 30
Average_marks =df['Marks'].mean()
Highest_score  =  df.loc[df['Marks'].idxmax()]
print(Average_marks)
print(Highest_score)
