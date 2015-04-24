__author__ = 'sci-lmw1'

# colour lookup example

colourDict = {}

inFile = open("colours.txt")
for line in inFile:
    parts = line.strip().split(", ")
    # print(parts)
    colourDict[parts[0]] = parts[1]

inFile.close()

# colour = input("Enter colour:")
# hexValue = input("Enter hex:")
# colourDict[colour] = hexValue
#
print(colourDict)

colourName = input("Colour name: ")
while colourName != "":
    print(colourName.capitalize(), "is", colourDict.get(colourName.lower(), "Unknown colour"))
    colourName = input("Colour name: ")