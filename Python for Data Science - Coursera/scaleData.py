import pandas as pd
import numpy as np

dataFrame = pd.read_csv("./data/census.csv")

groupBy_state = dataFrame.groupby("STNAME")
# Create the average and sum of population for each state in estimate 2010
# We can use the cut method provided by pandas to divide a col of dataframe into equally size of bins.

data_2010_pop = groupBy_state["CENSUS2010POP", "POPESTIMATE2010"].agg({"AVERAGE": np.average, "SUM": np.sum})
# The code below created 2 new cols in the dataframe, hold the rank of average and sum of POPESTIMATE2010 for all states
data_2010_pop["AVERAGE RANGE"] = pd.cut(data_2010_pop["AVERAGE"]["POPESTIMATE2010"], 3,
                                        labels=["SMALL", "MEDIUM", "LARGE"])
data_2010_pop["SUM RANGE"] = pd.cut(data_2010_pop["SUM"]["POPESTIMATE2010"], 3,
                                    labels=["SMALL", "MEDIUM", "LARGE"])
# This code get the states with low average but high sum of population
print(data_2010_pop[(data_2010_pop["AVERAGE RANGE"] == "SMALL") & (data_2010_pop["SUM RANGE"] == "LARGE")])
# This code get the state with high average but small sum of population
print(data_2010_pop[(data_2010_pop["AVERAGE RANGE"] == "LARGE") & (data_2010_pop["SUM RANGE"] == "SMALL")])
