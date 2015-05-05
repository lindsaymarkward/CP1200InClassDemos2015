__author__ = 'sci-lmw1'

# name = "Python"
# # t = tuple()
# print(name.upper())
# str("a")
# print(type(name))
# print(type([2, 3]))

""" BMI = Weight (kg) / (Height (m) x Height (m)) """

class Person():
    def __init__(self, name="", age=-1, height=0, weight=0):
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight

    def __str__(self):
        return self._name + ", " + str(self._age) + ". Height: " + str(self._height)

    def setName(self, name):
        self._name = name

    def setAge(self, age):
        self._age = age

    def setHeight(self, heightInMetres):
        self._height = heightInMetres

    def getName(self):
        return self._name

me = Person("Lindsay", 21, 1.76, 63)
# me.setName()
# me.setAge(21)
print(me.getName())
me.setHeight(1.80)

print(me)

friend = Person()
# friend.setName("Tim")
print(friend)

print("Hi " + str(me))