import fileinput

dictionary = {}
try:
    for line in fileinput.input(files = "CSV-Data.csv"):
        if fileinput.lineno() == 1:
            keys=line.split(",")
    else:
        row = (line.split(","))
        dictionary[str(row[0])] = {str(keys[1]):row[1],
                                  str(keys[2]):row[2],
                                  str(keys[3]):row[3],
                                  str(keys[4]):row[4],
                                  str(keys[5]):row[5]
                                  }
except FileNotFoundError :
    print("File not Found")
    exit()


def returnKeysFromDictionary():
    keys = list(dictionary.keys())
    return keys

def returnValuesInList(string):
    numbers = returnKeysFromDictionary
    list = []
    for numbers in dictionary:
        list.append(float(dictionary[numbers][string]))
    return list

def returnTotalPrice():
    totalPrice = 0
    prices = returnValuesInList("price")
    for price in prices:
        totalPrice = totalPrice + price
    return totalPrice

print("Total Price: " + str(returnTotalPrice()))

def returnCountNumberOfItems():
    numbers = returnCountNumberOfItems
    count = 0
    for numbers in dictionary:
        count = count+1
    return count

print("Number of Items: " + str(returnCountNumberOfItems()))

def returnAveragePrice():
    totalPrice=returnTotalPrice()
    count=returnCountNumberOfItems()
    average=totalPrice/count
    return average

print("Average Price: " + str(returnAveragePrice()))

def returnMaxValue(string):
    maximumQuantity=max(returnValuesInList(string))
    numbers = returnKeysFromDictionary()
    for numbers in dictionary:
        if maximumQuantity == float(dictionary[numbers][string]):
            return str(dictionary[numbers])

def returnMinValue(string):
    minimumQuantity=min(returnValuesInList(string))
    numbers = returnKeysFromDictionary()
    for numbers in dictionary:
        if minimumQuantity == float(dictionary[numbers][string]):
            return str(dictionary[numbers])

print("Maximum Quantity: " + returnMaxValue("quantity"))

print("Minimum Quantity: " + returnMinValue("quantity"))

print("Maximum Price: " + returnMaxValue("price"))

print("Minimum Price: " + returnMinValue("price"))
