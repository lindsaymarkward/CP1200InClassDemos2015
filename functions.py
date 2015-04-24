__author__ = 'sci-lmw1'

from math import sqrt


def main():

    password = input("Password: ")
    while not isValidPassword(password):
        print("No...")
        password = input("Password: ")

    print("You're in!")


def isValidPassword(password):
    secret = "YeS"
    return password == secret

    # if password == secret:
    #     return True
    # else:
    #     return False


# main()

def thingo():
    return 3, sqrt(49)

x, y, z = thingo()

print(type(x))