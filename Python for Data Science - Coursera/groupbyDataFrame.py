import pandas as pd
import time
import numpy as np

df = pd.read_csv("./data/census.csv")

# print(df)
df = df[df["SUMLEV"] == 50]
# Find average population of CENSUS2010POP by looping, using tradition for loop
begin = time.time()
for state in df["STNAME"].unique():
    average = np.average(df.where(df["STNAME"] == state).dropna()["CENSUS2010POP"])
    print(state + " has the average population in its counties is " + str(average))
print(time.time() - begin)

# Using groupby to calculate the CENSUS2010POP
begin = time.time()
for group, data in df.groupby("STNAME"):
    average = np.average(data["CENSUS2010POP"])
    print(group + " has the average population in its counties is " + str(average))
print(time.time() - begin)
# We can see that using groupby gives us a greater speed
print("======================================")


# We can only set the index of the dataframe, then pass to groupby a function to process the index somehow, and then
# group it.
# For example, if we want to group all counties in state with starting letter A, W together
# and the rest in another group
def classifyCounties(state):
    if state[0] == "A":
        return 1
    elif state[0] == "W":
        return 2
    else:
        return 0


df.set_index("STNAME", inplace=True)
for group, data in df.groupby(classifyCounties):
    print("There is " + str(len(data)) + " counties in group " + str(group))
# group1 = df.groupby(classifyCounties)
# print(group1.get_group(1))
print("========================================")


# if we want to find information about a certain columns and apply some method to that columns, then get the overview
# on the whole data, we can use the agg method on the groupby object
df.reset_index(inplace=True)
group_state = df.groupby("STNAME")
# Print the average of pop in for each state
print(group_state.agg({"CENSUS2010POP": np.average}))
print("+++++++++++++++++++")
# THE METHOD ABOVE CAN ONLY APPLY 1 FUNCTION TO EACH COLUMN.
# If we want to investigate multiple things, we can do it by indexing the cols from the groupby object first
print(group_state["CENSUS2010POP"].agg({"AVERAGE CENSUS2010": np.average, "SUM CENSUS2010": np.sum}))
# Apply for 2 cols instead of 1
print("++++++++++++++++++")
print(group_state[["CENSUS2010POP", "POPESTIMATE2010"]].agg({"AVERAGE": np.average, "SUM": np.sum}))
# Below is how to extract information from a specific cell.
groupby_state2 = group_state[["CENSUS2010POP", "POPESTIMATE2010"]].agg({"AVERAGE": np.average, "SUM": np.sum})
# print(groupby_state2.loc["New York"]["AVERAGE"]["CENSUS2010POP"])
