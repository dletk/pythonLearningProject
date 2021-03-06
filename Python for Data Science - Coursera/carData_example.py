import csv

def findAverageCityMPG(carDataList):
    sumCityMPG = sum(float(car["cty"]) for car in carDataList)
    return sumCityMPG/len(carDataList)


def findAverageCityMPGbyCylinder(carDataList):
    cylinder = {car["cyl"]:[] for car in carDataList}
    listResult = []
    for car in carDataList:
        cylinder[car["cyl"]].append(float(car["cty"]))
    for cyl in cylinder:
        cylinder[cyl] = sum(cylinder[cyl])/len(cylinder[cyl])
        listResult.append((cyl,cylinder[cyl]))
    listResult.sort(key=lambda x: x[0])
    return listResult


def findAverageHWYbyClass(carDataList):
    classes = {car["class"]: [] for car in carDataList}
    listResult = []
    for car in carDataList:
        classes[car["class"]].append(float(car["hwy"]))
    for cls in classes:
        sumValue = sum(classes[cls])
        listResult.append((cls,sumValue/len(classes[cls])))
    listResult.sort(key= lambda x: x[1])
    return listResult

if __name__ == '__main__':
    with open("./data/mpg.csv") as carData:
        carDataList = list(csv.DictReader(carData))
    print(carDataList)
    print(carDataList[0].keys())
    print("Average CITY MPG for all cars in data: "+str(findAverageCityMPG(carDataList)))
    print(findAverageCityMPGbyCylinder(carDataList))
    print(findAverageHWYbyClass(carDataList))
