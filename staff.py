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

'''
Staff class:
- Attributes: name, staff ID, role.
'''
class Staff:

    def __init__(self, name, staff_id, role):
        self.__name = name
        self.__staff_id = staff_id
        self.__role = role

    '''
    Getters:
    '''
    def get_name(self):
        return self.__name

    def get_staff_id(self):
        return self.__staff_id

    def get_role(self):
        return self.__role

    '''
    Setters:
    '''
    def set_name(self, name):
        self.__name = name

    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    def set_role(self, role):
        self.__role = role

    def __str__(self):
        return f"{self.__name} {self.__role}"

'''
Zookeeper class:
- Attributes: enclosures assigned to them.
'''
class Zookeeper(Staff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Zookeeper")
        self.__enclosures = []

    '''
    get_enclosures: 
    Returns list of enclosures.
    '''
    def get_enclosure(self):
        return list(self.__enclosures)

    def set_enclosure(self, enclosure):
        self.__enclosures = enclosures

    '''
    assign_enclosure: 
    Adds an enclosure to the zookeeper's list.
    '''
    def assign_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            if enclosure not in self.__enclosures:
                self.__enclosures.append(enclosure)

    '''
    feed_animal: 
    Makes the zookeeper feed an animal.
    '''
    def feed_animal(self, animal):
        if isinstance(animal, Animal):
            return f"{self.get_name()} feed {animal.get_name()}. {animal.eat()}"

    '''
    clean_enclosure: 
    makes the zookeeper clean an enclosure.
    '''
    def clean_enclosure(self, enclosure):
        if enclosure in self.__enclosures:
            enclosure.clean()
            return f"{self.get_name()} cleared {enclosure.get_name()}"

    '''
    get_summary(): shows all enclosures this zookeeper manages.
    '''
    def get_summary(self):
        if self.__enclosures:
            names = ", ".join(a.get_name() for a in self.__enclosures)
        else:
            names = "None"

        return f"{self.get_name()} | Enclosures: {names}"

'''
Veterinarian class:
- Attributes: animals receiving treatment.
'''
class Veterinarian(Staff):

    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Veterinarian")
        self.__animals = []

    '''
    get_animals: 
    List of animals being treated.
    '''
    def get_animals(self):
        return list(self.__animals)

    def set_animals(self, animals):
        self.__animals = animals

    '''
    record_health_issue: 
    Adds a health issue to an animal.
    '''
    def record_health_issue(self, animal, description, severity, treatment):
        if isinstance(animal, Animal):
            issue = animal.add_health_issue(description, severity, treatment)

            if animal not in self.__animals:
                self.__animals.append(animal)

            return f"{self.get_name()} added issued for {animal.get_name()}: {issue.get_description()}"

    '''
    resolve_all_issues: 
    Resolves every health issue an animal has.
    '''
    def resolve_all_issues(self,animal, notes=""):
        issues = animal.get_health_issues()
        for i in range(len(issues)):
            if not issues[i].get_resolved():
                animal.resolve_health_issue(i, notes)

        return f"{self.get_name()} resolved all issues for {animal.get_name()}"

    '''
    get_summary: 
    List of animals under treatment by this vet.
    '''
    def get_summary(self):
        if self.__animals:
            names = ", ".join(a.get_name() for a in self.__animals)
        else:
            names = "None"

        return f"{self.get_name()} | Animals: {names}"

