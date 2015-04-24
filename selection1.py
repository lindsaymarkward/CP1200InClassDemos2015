__author__ = 'sci-lmw1'

age = int(input("Age: "))
# if age is valid
if age >= 0 and age <= 120:
    if age >= 18:
        print("You're in!")
        isAdult = True
    else:
        print("Sorry...")
        isAdult = False
else:
    print("Invalid age!")

# if age is invalid
if age < 0 or age > 120:
    print("Invalid age!")
else:
    print("OK")