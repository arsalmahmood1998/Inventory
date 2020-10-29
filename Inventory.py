import fileinput

dictionary = {}
for line in fileinput.input(files = "CSV-Data.csv"):
    if fileinput.lineno() != 1:
        row = (line.split(","))
        dictionary[row[0]] = {"Title":row[1],
                         "Description":row[2],
                         "Code":row[3],
                         "Price":row[4],
                         "Quantity":row[5]
                         }

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
    prices = returnValuesInList("Price")
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

print("Maximum Quantity: " + returnMaxValue("Quantity"))

print("Minimum Quantity: " + returnMinValue("Quantity"))

print("Maximum Price: " + returnMaxValue("Price"))

print("Minimum Price: " + returnMinValue("Price"))
