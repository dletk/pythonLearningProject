import pandas as pd
import numpy as np
import time

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
    print("====================================================")
    # Querying a series
    series_3 = pd.Series(classStu)
    print(series_3)
    print("Querying a series using numeric location is similar to matrix/array:")
    print(series_3.iloc[3])
    print("Querying a series ussing index label:")
    print(series_3.loc["Duc"])
    print("====================================================")
    # Looping through a series in a traditional for loop
    listNum = np.random.randint(1,10000,1000)
    series_4 = pd.Series(listNum)
    print(series_4.head(10))
    print("++++++++++++++")
    for item in series_4:
        print(item)
    print("====================================================")
    # Updating all element in a series with a constant value, with tradition for loop (slow)
    begin = time.time()
    for label, value in series_4.iteritems():
        series_4.loc[label] = value + 2
    print("Time: "+str(time.time()-begin)+" s")
    # Updating all element in a series with a constant value, vectorization (fast)
    begin = time.time()
    series_4 += 2
    print("Time: "+str(time.time()-begin)+" s")
    print("====================================================")
    # Using loc to adding new item that is not in the series, if the item is in different type, Pandas will automatically
    # change the type of the series.
    series_5 = pd.Series([1,2,3,4,5])
    print(series_5)
    series_5.loc["Duc"] = "Sophomore"
    print(series_5)
    print("====================================================")
    # Index in series does not need to be unique. There can be multiple values with the same index
    series_6 = pd.Series(["Duc","Trung","Giang","Que"],["Sophomore","Sophomore","Sophomore","Sophomore"])
    print(series_6)
    print(series_6.loc["Sophomore"])
    newSeries = series_5.append(series_6)
    # Keep in mind that append a series will return a new series, it does not change the original series.
    print(series_5)
    print(newSeries)
    print(newSeries.loc["Sophomore"])
