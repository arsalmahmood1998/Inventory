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

def value(rowNum,columnNum):
    if rowNum == 1:
        values = list (dict.keys())
        print("value1: "+values[columnNum-1])
        return values[columnNum-1]

    else:
        values = dict[titles[columnNum-1]]
        if rowNum <= 0 and columnNum >0:
            return values[rowNum-2],(len(values)+1) + rowNum,columnNum
        else:
            print("value4: "+values[rowNum-2])
            return values[rowNum-2]

print(value(-2,4))
