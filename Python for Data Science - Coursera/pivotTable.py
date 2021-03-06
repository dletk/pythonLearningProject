import pandas as pd
import numpy as np

dataFrame_car = pd.read_csv("./data/cars.csv")

# print(dataFrame_car.head())
# print(dataFrame_car.set_index(["Make", "Size"]))
# groupby_make_size = dataFrame_car.groupby(["Make", "Size"])
# print(groupby_make_size.groups)
# print(np.average(groupby_make_size.get_group(("TESLA", "FULL-SIZE"))["CITY (kWh/100 km)"]))

# dataFrame_car.set_index("YEAR", inplace=True)
groupby_year_make = dataFrame_car.groupby(["YEAR", "Make"])

print(groupby_year_make.get_group((2013, "FORD")))