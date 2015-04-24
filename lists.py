__author__ = 'sci-lmw1'


def formatString2(things, separator):
    string = ""

    for thing in things[:-1]:
        string += str(thing) + separator
    string += str(things[-1])
    return string


def formatString(things, separator):
    string = ""

    for thing in things:
        string += str(thing) + separator
    return string[:-len(separator)]

# print(formatString([1, 2, 3], '----'))
# print(formatString2([1, 2, 3], '----'))
# print(formatString([], '!!!'))


# name = input("Name: ")
# while True:
#     choice = input("Char: ")
#     while len(choice) != 1:
#         print("One char please")
#         choice = input("Char: ")
#
#     if choice in list(name):
#         print("Yes, that's in your name.")
#     else:
#         print("No.")
