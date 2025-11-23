'''
File: filename.py
Description: A brief description of this Python module.
Author: Amitoj Dhillon
ID: 110100110
Username: Dhiay010
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal
from enclosure import Enclosure

class Staff:

    def __init__(self, name, staff_id, role):
        self.__name = name
        self.__staff_id = staff_id
        self.__role = role


    def get_name(self):
        return self.__name

    def get_staff_id(self):
        return self.__staff_id

    def get_role(self):
        return self.__role


    def set_name(self, name):
        self.__name = name

    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    def set_role(self, role):
        self.__role = role

    def __str__(self):
        return f"{self.__name} {self.__role}"

class Zookeeper(Staff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Zookeeper")
        self.__enclosures = []

    def get_enclosure(self):
        return list(self.__enclosures)

    def set_enclosure(self, enclosure):
        self.__enclosures = enclosures

    def assign_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            if enclosure not in self.__enclosures:
                self.__enclosures.append(enclosure)

    def feed_animal(self, animal):
        if isinstance(animal, Animal):
            return f"{self.__get_name()} feed {animal.__get_name()}. {animal.eat()}"

    def clean_enclosure(self, enclosure):
        if enclosure in self.__enclosures:
            enclosure.clean()
            return f"{self.__get_name()} cleared {enclosure.get_name()}"

    def get_summary(self):
        if self.__enclosures:
            names = ", ".join(a.get_name() for a in self.__enclosures)
        else:
            names = "None"

        return f"{self.__get_name()} | Enclosures: {names}"
