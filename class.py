class Item():
    def __init__(self,id,title,description,code,price,quantity):
        self.id = id
        self.title = title
        self.description = description
        self.code = code
        self.price = price
        self.quantity = quantity

    def printDetails(self):
        message = "This item has id: " + self.id + "\n"
        message = message +  "Quantity: " + self.quantity + "\n"
        message = message +  "Price: " + self.price + "\n"
        message = message +  "Title: " + self.title + "\n"
        message = message + "Code: " + self.code + "\n"
        message = message + "Description: " + self.description + "\n"
        return message

try:
    file = open("CSV-Data.csv","r")
except FileNotFoundError :
    print("File not Found")
    exit()

dict = {}
for index,line in enumerate(file):
        if index != 0:
            values = line.split(",")
            item = Item (values[0],values[1],values[2],values[3],values[4],values[5])
            dict[index] = item

def returnTotalNumberOfItems():
    count=0
    keys = list(dict.keys())
    for key in keys:
        value = int(dict[key].id)
        count = count + 1
    return count

print("Total number of items: "+ str(returnTotalNumberOfItems()))

def sumOfPrices():
    sum=0
    keys = list(dict.keys())
    for key in keys:
        sum = sum + float(dict[key].price)
    return sum

print("Total sum of prices: "+ str(sumOfPrices()))
