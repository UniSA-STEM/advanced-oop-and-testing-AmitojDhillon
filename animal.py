'''
File: animal.py
Description: A brief description of this Python module.
Author: Amitoj Dhillon
ID: 110100110
Username: Dhiay010
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:

    def __init__(self, name, species, age, diet, environment_type):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__environment_type = environment_type
        self.__on_display = False
        self.__health_issues = []


    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_diet(self):
        return self.__diet

    def get_environment_type(self):
        return self.__environment_type

    def get_on_display(self):
        return self.__on_display

    def get_health_issues(self):
        return list(self.__health_issues)

    def set_name(self, name):
        self.__name = name

    def set_species(self, species):
        self.__species = species

    def set_age(self, age):
        self.__age = age

    def set_diet(self, diet):
        self.__diet = diet

    def set_environment_type(self, environment_type):
        self.__environment_type = environment_type

    def set_on_display(self, on_display):
        self.__on_display = on_display



