__author__ = 'sci-lmw1'


def main():
    age = int(input("Age: "))
    printAverage(age, 7)
    printString("Test", 4)


def printString(string, numberOfTimes):
    print(string * numberOfTimes)

# printString("Lindsay", 4)
# printString("Hi", 17)


def printAverage(number1, number2):
    print((number1 + number2) / 2)
    # print(age)

main()