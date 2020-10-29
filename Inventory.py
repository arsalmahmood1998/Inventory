file=open("New CSV-Data.csv","r")

dictionary = {}

try:
    for index,line in enumerate(file):
        if index == 0:
            titles =line.split(",")
        else:
            dictionary[index] = {}
            row =(line.split(","))
            for j in range(len(titles)-1):
                dictionary[index][titles[j]] = row[j]

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
