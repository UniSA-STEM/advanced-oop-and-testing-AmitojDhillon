'''
File: filename.py
Description: A brief description of this Python module.
Author: Amitoj Dhillon
ID: 110100110
Username: Dhiay010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Enclosure:

    def __init__(self, name, size, environment_type, max_animals, allowed_species):
        self.__name = name
        self.__size = size
        self.__environment_type = environment_type
        self.__max_animals = max_animals
        self.__allowed_species = allowed_species
        self.__cleanliness = 100
        self.__animals = []


    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_environment_type(self):
        return self.__environment_type

    def get_max_animals(self):
        return self.__max_animals

    def get_allowed_species(self):
        return self.__allowed_species

    def get_cleanliness(self):
        return self.__cleanliness

    def get_animals(self):
        return list(self.__animals)

    def set_name(self, name):
        self.__name = name

    def set_size(self, size):
        self.__size = size

    def set_environment_type(self, environment_type):
        self.__environment_type = environment_type

    def set_max_animals(self, max_animals):
        self.__max_animals = max_animals

    def set_allowed_species(self, allowed_species):
        self.__allowed_species = allowed_species

    def set_cleanliness(self, cleanliness):
        self.__cleanlines = cleanliness


    def is_full(self):
        return len(self.__animals) >= self.__max_animals
