import pandas as pd
import numpy as np

print("Creating a 3 series by dictionary, with name of customer, item, and cost as index")
purchase_1 = pd.Series({"Name": "Duc", "Item": "Lamborghini", "Cost": "300,000usd"})
purchase_2 = pd.Series({"Name": "Trung", "Item": "Mercedes", "Cost": "250,000usd"})
purchase_3 = pd.Series({"Name": "Giang", "Item": "Nintendo", "Cost": "250usd"})

dataFrame_1 = pd.DataFrame([purchase_1, purchase_2, purchase_3],["Euro Auto", "Germany Auto", "Gamestore"])

print(dataFrame_1)

# Querying the data from the dataFrame using loc
print("===============================================")
print(dataFrame_1.loc["Euro Auto"])
# Checking the type of the data we just queried
print(type(dataFrame_1.loc["Euro Auto"]))
# The indices can be the same for different values, it does not need to be unique
print("===============================================")
purchase_4 = pd.Series({"Name": "Trinh", "Item": "Porsche", "Cost": "350,000usd"})
purchase_4.name = "Euro Auto"
dataFrame_1 = dataFrame_1.append(purchase_4)
print(dataFrame_1)
print("===============================================")
print(dataFrame_1.loc["Euro Auto"])
print("===============================================")
# iloc and loc are used for row selection, and indexing operator is used for column selection
print([dataFrame_1["Item"]])
print("+++++++++++++++++++++")
print(dataFrame_1.loc["Euro Auto","Cost"])
# loc can also be used for slicing, and getting the columns that we are interested in.
print(dataFrame_1.loc["Germany Auto":"Gamestore", ["Name", "Item"]])
print("===============================================")
# Using drop to delete element from the dataFrame, it will return a new copy if the arg inplace set to false, or update
# the original dataFrame directly if the inplace set to true. Using 1 (instead of 0 as default) for axis to delete cols
newData = dataFrame_1.copy()
newData = newData.drop("Gamestore")
print(newData)
dataFrame_1.drop("Cost",1,inplace=True)
print(dataFrame_1)
print("===============================================")
# We can delete a column with indexing operator also. REMEMBER indexing operator can be used to access cols only
# It will have immediate effect to the original dataframe instead of return a copy of it.
del dataFrame_1["Name"]
print(dataFrame_1)
print("===============================================")
# Finally, we can add new cols to the dataframe with indexing operator
dataFrame_1["Name"] = ["Duc", "Trung", "Giang", "Trinh"]
print(dataFrame_1)
dataFrame_1["Location"] = None
print(dataFrame_1)