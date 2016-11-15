import pandas as pd
import numpy as np

data_log = pd.read_csv("./data/log.csv",)

# print(data_log)
# There are a lot of missing values in the paused and volume columns of this dataFrame
# There is a function to deal with missing values in pandas, fillna
# There is different ways of using fillna
data_log_copy = pd.DataFrame(data_log.copy())
# Replace all the missing data with -1
data_log_copy.fillna(-1,inplace=True)
print(data_log_copy.head())
print("================================")
data_log.set_index("time",inplace=True)
# Sort by the index
data_log.sort_index(inplace=True)
print(data_log)
# The index in this case is not unique, since there can be users using the system at the same time
# This may not be useful, so we will use multilevel index
print("================================")
data_log.reset_index(inplace=True)
# data_log.set_index(["time", "user"],inplace=True)
print(data_log["user"])
