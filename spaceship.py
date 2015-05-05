__author__ = 'sci-lmw1'


class Spaceship:
    def __init__(self, name="", crewCapacity=0, currentCrew=0, speed=0):
        self._name = name
        self._crewCapacity = crewCapacity
        self._currentCrew = currentCrew
        self._speed = speed

    def __str__(self):
        """ Example: Serenity – 4 crew – goes 300km/hr """
        return self._name + " - " + str(self._crewCapacity) + " crew - goes " + \
            str(self._speed) + " km/hr"

    def getName(self):
        return self._name

    def hasSpareCapacity(self):
        return self._currentCrew < self._crewCapacity
