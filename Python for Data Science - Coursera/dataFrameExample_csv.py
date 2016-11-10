import pandas as pd
import numpy as np

# Index_col indicate which cols should be used as index for the dataFrame, and header indicate which row should be used
# for the index of the cols. Instead of header, we can use skiprows = 1.
dataFrame_in = pd.read_csv("./data/olympics.csv", index_col=0, header=1)
# print(dataFrame_in.head(10))
# Getting the cols name in pandas
print(dataFrame_in.columns)
for col in dataFrame_in.columns:
    if col[:1] == "№":
        dataFrame_in.rename(columns={col: "#" + col[2:]}, inplace=True)
    elif col[:2] == "01":
        dataFrame_in.rename(columns={col: "Gold" + col[4:]}, inplace=True)
    elif col[:2] == "02":
        dataFrame_in.rename(columns={col: "Silver" + col[4:]}, inplace=True)
    elif col[:2] == "03":
        dataFrame_in.rename(columns={col: "Bronze" + col[4:]}, inplace=True)

print(dataFrame_in.head(5))
# Using boolean masking to query the dataframe
print("======================================")
# Example: Taking the countries that have gold medal in summer olympic
# Using the indexing operator we have:
print(dataFrame_in["Gold"] > 0)
print("======================================")
# With the boolean mask above, we can use the where function to take out the name of country.
# The where function takes the Boolean mask as condition, apply it to the dataFrame or series, and return the dataFrame
# or series with same shape.
# All the index with value meet the condition will have the data stay the same, whereas the countries that do not
# meet the condition will have all data change to NaN instead.
# THIS WORKS BECAUSE MOST OF STATISTICAL FUNCTION IN DATAFRAME IGNORE THE VALUE OF NAN.
gold_on_summer = dataFrame_in.where(dataFrame_in["Gold"] > 0)
print(gold_on_summer)
print(gold_on_summer["Gold"].count())
print("======================================")
# We can drop the non data value by using dropna
gold_on_summer = gold_on_summer.dropna()
print(gold_on_summer.head(10))
print("======================================")
# Also, we can do use the indexing operator with the boolean mask directly without the where function
# NOTE: Use this way instead, there will be no NaN values to worry like the where function
gold_on_summer = dataFrame_in[dataFrame_in["Gold"] > 0]
print(gold_on_summer.head(5))
print("======================================")
# You can combine the boolean masks together USING BITWISE OPERATOR to have a general boolean mask
# REMEMBER THE BRACKET WHEN USING BITWISE
gold_on_all = dataFrame_in[(dataFrame_in["Gold"] > 0) & (dataFrame_in["Gold.1"] > 0) & (dataFrame_in["Gold.2"] > 0)]
print(gold_on_all)
print("+++++++++++++++++++++++++++++++++++++")
gold_winter_no_summer = dataFrame_in[(dataFrame_in["Gold"] == 0) & (dataFrame_in["Gold.1"] > 0)]
print(gold_winter_no_summer)
# Only Liechtenstein
print("======================================")
# Changing the index to gold earned in summer
dataFrame_in["Country"] = dataFrame_in.index
data = dataFrame_in.set_index("Gold")
print(data.head(5))
# Get rid of the index completely and index by number
print(dataFrame_in.reset_index())
print("=============================================================================================================")
# Using multi-level index
dataFrame_in_2 = pd.read_csv("./data/census.csv")
print(dataFrame_in_2.head())
print(dataFrame_in_2["SUMLEV"].unique())
# The unique level of col SUMLEV are only 40 and 50. 40 means that rows is the data of the state, 50 is the data of
# county in the state. We will eliminate the 40 and only works with county data
dataFrame_in_2 = dataFrame_in_2[dataFrame_in_2["SUMLEV"] == 50]
print(dataFrame_in_2.head())
# We will only work with the total pop and total birth estimate to reduce the size of data
dataFrame_in_2 = dataFrame_in_2[['STNAME',
                                 'CTYNAME',
                                 'BIRTHS2010',
                                 'BIRTHS2011',
                                 'BIRTHS2012',
                                 'BIRTHS2013',
                                 'BIRTHS2014',
                                 'BIRTHS2015',
                                 'POPESTIMATE2010',
                                 'POPESTIMATE2011',
                                 'POPESTIMATE2012',
                                 'POPESTIMATE2013',
                                 'POPESTIMATE2014',
                                 'POPESTIMATE2015']]
print("======================================")
print(dataFrame_in_2.head())
print("======================================")
# Now we want to create an index combining the state name and county name
cols_index = ["STNAME","CTYNAME"]
dataFrame_in_2 = dataFrame_in_2.set_index(cols_index)
print(dataFrame_in_2.head())
print("======================================")
# data_Michigan = dataFrame_in_2.loc["Michigan"].copy()
# print(dataFrame_in_2.loc["Michigan"])
print(dataFrame_in_2.loc["Michigan","Wayne County"])
print(dataFrame_in_2.loc[["Michigan","Alabama"]])
# print(dataFrame_in_2.loc[[("Michigan", "Wayne County"),("Michigan","Bay County")]])
