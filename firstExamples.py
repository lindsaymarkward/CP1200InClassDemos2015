# My first examples in CP1200

__author__ = 'sci-lmw1'

YEARS_LATER = 100


def main():
    age = 21
    # firstName = input("What is your name: ")
    firstName = "Bob"
    printGreeting(firstName)

    # age = int(input("What is your age: "))
    print("Hello \"", firstName, "\".\nYou are ", age, " years old.", sep='')
    nextDecadeAge = age + YEARS_LATER
    printNextAge(YEARS_LATER, nextDecadeAge)
    printClosing()
    print(firstName)


def printNextAge(years, age):
    print("In", years, "years you'll be", age, "years old")


def printLine():
    print()
    print("-" * 110)


def printClosing():
    printLine()

def printGreeting(name):
    print("Hello", name)
    printLine()
    name = "Blah!!"

# printGreeting("Lindsay")
# printGreeting("Patrick")
# print("Hello CP1200")


main()