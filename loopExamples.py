__author__ = 'sci-lmw1'

# number = 0
#
# while number < 10:
#     print(number)
#     number = number + 1
#
# print("Last:", number)
#
# number = 10
# while number > 0:
#     print(number)
#     number = number - 1
# print("Blast Off!")

# print(list(range(10)))
# print(list(range(1, 10)))
# print(list(range(1984, 2020, 4)))

# for i in range(3):
#     print("Hello")

# numbers = [3, 4, -1, 0, 9, 123, 55]
#
# total = 0
# for number in numbers:
#     total += number
#
# print(total)

startYear = int(input("Start "))
endYear = int(input("End "))
while endYear < startYear:
    print("Error. End must be >= Start")
    endYear = int(input("End "))

for year in range(startYear, endYear + 1, 4):
    print(year)


# for i in range(10):
#     print(i)


# total = 0
# count = 0
# age = int(input("Age: "))
# while age >= 0:
#     total += age
#     count += 1
#     age = int(input("Age: "))
# if count != 0:
#     print("total", total)
#     print("average", total / count)
# else:
#     print("no total or average")
#
