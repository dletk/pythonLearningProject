import csv

def ctyByClass(listCars):
    ctyClasses = {}
    for car in listCars:
        if car["class"] in ctyClasses:
            ctyClasses[car["class"]].append(float(car["hwy"]))
        else:
            ctyClasses[car["class"]] = [float(car["hwy"])]
    for cls in ctyClasses:
        ctyClasses[cls] = sum(ctyClasses[cls])/len(ctyClasses[cls])

    listSorted = sorted(ctyClasses.items(),key = lambda x: x[1])

    return listSorted

if __name__ == '__main__':
    with open("./data/mpg.csv") as csvFile:
        listCars = list(csv.DictReader(csvFile))
    print(listCars)
    print(listCars[0].keys())
    print(ctyByClass(listCars))