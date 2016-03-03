def characterValues():
    rawValues = open('/Users/hgoscenski/Desktop/characterValues.txt', 'r')
    temp = []
    rowValueDict = {}
    columnValueDict = {}
    for line in rawValues:
        temp.append(line.split())
    charValues = dict(zip(temp[0][0::2], temp[0][1::2]))
    for i,x in enumerate(temp[1]):
        rowValueDict[i] = x
    for i,x in enumerate(temp[2]):
        columnValueDict[i] = x
characterValues()



# print(charValues)
# tempLetter = []
# tempValue = []
# for i,x in temp[0]:
#     if i % 2 == 0:
#         tempLetter.append(x)
#     else:
#         tempValue.append(x)
