import pandas as pd
import numpy as np

dataFrame_1 = pd.DataFrame([{"Name": "Chris", "Items purchased": "Sponge", "Cost": 22.5},
                            {"Name": "Kevyn", "Items purchased": "Kitty Litter", "Cost": 2.5},
                            {"Name": "Fliip", "Items purchased": "Spoon", "Cost": 5}],
                           index=["Store 1", "Store 2", "Store 3"])
print(dataFrame_1)
dataFrame_1["Date"] = ["Januray 2nd", "December 12th", "October 14th"]
print(dataFrame_1)
# Setting a default value for a new column only applicable for scalar value
dataFrame_1["Delivered"] = True
print(dataFrame_1)
print("=================")
# If we only want to update a few values in a columns, we have to use the None value
dataFrame_1["Feedback"] = ["Positive", None, "Negative"]
print(dataFrame_1)
# Or, we can use the index and the column identifier to assign new value to some index and ignore the other
# This only work if our dataFrame has unique indices
dataFrame_1["Date"] = pd.Series({"Store 1": "Feb 6th", "Store 3": "Jun 6th"})
print("=================")
# Pandas will put missing value NaN in to the ignored indices for us
print(dataFrame_1)
print("===================================================")
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df.set_index('Name', inplace=True)
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df.set_index('Name', inplace=True)
# print(staff_df)
# print(student_df)
# The code below will get the union of 2 dataFrame
all_people = pd.merge(student_df, staff_df, 'outer', left_index=True, right_index=True)
print(all_people)
print("===================================================")
# The code below will get the intersection of the dataframe
staff_student = pd.merge(staff_df, student_df, 'inner', left_index=True, right_index=True)
print(staff_student)
print("===================================================")
# Commonly, we will want to use the index of 1 dataFrame but want to see the information in the other dataFrame if the
# index is in that dataFrame also, we will use the how = left or right to do so with left_index or right_index
staff_all_info = pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
print(staff_all_info)
print("===================================================")
# Instead of index, we can use any column of the 2 dataFrame to merge them
staff_df.reset_index(inplace=True)
student_df.reset_index(inplace=True)
by_col = pd.DataFrame(pd.merge(staff_df, student_df, 'left', left_on='Name', right_on='Name')).set_index('Name')
print(by_col)
print("===================================================")
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
# These 2 dataFrame above have conflict in their data, where the data of location in dataFrame 1 is the office address
# and the location in dataframe 2 is the home address. In this case, pandas will use the _x and _y to indicate the data,
# with _x is data from left and _y is data from right
data_withLocation = pd.DataFrame(pd.merge(staff_df, student_df, how='inner', left_on='Name', right_on='Name')).set_index('Name')
print(data_withLocation)
print("===================================================")
# MULTI-INDEX AND MULTIPLE COLS
staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
# 2 data frame above have some people with same first name but different last name, we want to merge them in a correct
# way using the merge fuction and multiple key for left_on and right_on
data_merge = pd.DataFrame(pd.merge(staff_df, student_df, how='inner', left_on=['First Name', 'Last Name'], right_on=['First Name', 'Last Name']))
print(data_merge)
print("===================================================")
# Using function apply for dataFrame to apply a fuction to every row of the dataFrame
df = pd.read_csv("./data/census.csv")
df = df[df["SUMLEV"]==50]
df.set_index(["STNAME", "CTYNAME"], inplace=True)
# print(df.head())

def max_min(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({"MIN": np.min(data), "MAX": np.max(data)})

df = df.apply(max_min, axis=1)
print(df)