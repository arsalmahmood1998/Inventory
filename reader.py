try:
    file = open("New CSV-Data.csv","r")
except FileNotFoundError :
    print("File not Found")
    exit()

dict = {}
for index,line in enumerate(file):
        if index == 0:
            titles = line.split(",")
            for title in titles:
                dict[title] = []
        else:
            row = (line.split(","))
            for j in range(len(row)-1):
                dict[titles[j]].append(row[j])

def sum(columnName):
    list = dict[columnName]
    sum = 0
    try:
        for i in range(len(list)):
            sum = sum + float(list[i])
    except ValueError:
        return 0
    return sum

print("Sum of Price: "+ str(sum("price")))

def average(columnName):
    count = len(dict[columnName])
    total = sum(columnName)
    try:
        average = total / count
    except TypeError:
        return 0
    return average

print("Average of Price: " + str(average("price")))

def minimumQuantity(columnName):
    column = dict[columnName]
    minQuantity = 999999999999.0
    for i in range (len(column)):
        value = float(column[i])
        if value < minQuantity:
            minQuantity = value
    return minQuantity

print("Minimum Value of price: " + str(minimumQuantity("price")))
print("Minimum Value of quantity: " + str(minimumQuantity("quantity")))

def maximumQuantity(columnName):
    column = dict[columnName]
    maxQuantity = -999999999999.0
    for i in range (len(column)):
        value = float(column[i])
        if value > maxQuantity:
            maxQuantity = value
    return maxQuantity

print("Maximum Value of price: "+ str(maximumQuantity("price")))
print("Maximum Value of quantity: "+ str(maximumQuantity("quantity")))

count = len(dict["id"])
print("Total number of Items: " + str(count))

def value(rowNum,columnNum):
    if rowNum == 1:
        values=list(dict.keys())
        return values[columnNum-1]
    else:
        values = dict[titles[columnNum-1]]
        if rowNum <= 0:
            return values[rowNum-2],values.index(values[rowNum])+2,titles.index(titles[columnNum])
        return values[rowNum-2]

print("Your required value is: " + str(value(-6,-5)))
