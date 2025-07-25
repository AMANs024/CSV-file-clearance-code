# (Example of array and table)
# import numpy as np
# import pandas as pd
# arr = np.array([1 ,2 ,3])
# print("NumPy Array:" , arr)
# data = {'Name' : ['aman' , 'siddesh'], 'Sir name' : ['sheikh','Dhumal'] , 'Score': [85, 90]}
# df = pd.DataFrame(data)
# print("Pandas DataFrame:\n", df)


#(Example of array maths)
# import numpy as np
# a = np.array([1,2,3,4,5])
# b = np.array([3,4,5,6,7])
# print("Addition:" , a+b)
# print("Substraction:" , a-b)
# print("Mean of A" , np.mean(a))


#(Example for generating random data)
# import numpy as np
# arr = np.random.randint(1, 100, size=(5, 5))
# print("Random Array:\n", arr)
# print("Max value in each row:", np.max(arr, axis=1))

# (Example for pandas library)
# import pandas as pd
# data = {
#     'Name': ['Aman', 'Aman'],
#     'Marks': [85, 90, 78],
#     'Grade': ['B', 'A', 'C']
# }
# df = pd.DataFrame(data)
# # Filter rows
# print(df[df['Marks'] > 80])


#(creating and playing with csv files)
# import pandas as pd
# df = pd.read_csv('student.csv')
# print(df.head())
# # Drop a column
# df = df.drop('Grade', axis=1)
# # Add new column
# df['Pass'] = df['Marks'] >= 40
# print(df)

# Input: CSV file with student names and marks
# Task: Calculate average, highest scorer, and pass/fail status

import pandas as pd
df = pd.read_csv('student.csv')
print(df.head())
print(df)
# Case1:To check if the Students are pass or fail
df['Pass'] = df['Marks'] >= 30
Average_marks =df['Marks'].mean()
Highest_score  =  df.loc[df['Marks'].idxmax()]
print(Average_marks)
print(Highest_score)
