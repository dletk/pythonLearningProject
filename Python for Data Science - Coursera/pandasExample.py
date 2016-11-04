import pandas as pd
import numpy as np

if __name__ == '__main__':
    # Creating a series using an array, pandas will automatically assign the index
    animals = ["Tiger", "Bear", "Moose"]
    print(pd.Series(animals))
    number = [1,2,3,4,5]
    print(pd.Series(number))
    animals = ["Tiger", "Bear", None]
    print(pd.Series(animals))
    number = [1,2,3,4, None]
    print(pd.Series(number))
    print(np.nan == np.nan)
    print(np.isnan(np.nan))
    # Creating a series from a dictionary, pandas will use the key to be the index
    print("====================================================")
    classStu = {"Duc": "Sophomore", "DAN": "Freshman", "Trung": "Junior"}
    se = pd.Series(classStu)
    print(se)
    # Getting the index object of the series using index attribute
    print(se.index)
    # Creating a series by passing the index explicitly with the array
    print("====================================================")
    se2 = pd.Series(["Duc","Trung","DAN"],["Sophomore","Junior","Freshman"])
    print(se2)
    print("====================================================")
    # If we pass in a dictionary and an index list, but some keys in the index list is not in the dictionary, Pandas
    # will favor the index list that we put in. It means that it will create a series with all index value from the
    # index list associated with the value that index matches in the input dictionary, if there is no match, it will
    # assign the value None or NaN for that key. Other key that is not in the index list will be ignored.
    classStu = {"Duc": "Sophomore", "DAN": "Freshman", "Trung": "Junior", "Chi":"Senior"}
    se3 = pd.Series(classStu,["Duc", "DAN", "Trung", "Giang"])
    # Giang is assigned the value NaN, while Chi is completely ignored from the series
    print(se3)
