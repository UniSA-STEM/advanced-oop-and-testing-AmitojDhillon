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
        if on_display and self.active_health_issues():
            return
        self.__on_display = on_display

    def add_health_issue(self, description, severity, treatment):
        issue = HealthIssue(description, severity, treatment)
        self.__health_issues.append(issue)
        self.__on_display = False
        return issue

    def active_health_issues(self):
        for issue in self.__health_issues:
            if not issue.is_active():
                return True
            return False

    def resolve_health_issue(self, index, notes=""):
        if 0 <= index < len(self.__health_issues):
            self.__health_issues[index].mark_resolved(notes)

    def can_move(self):
        return not self.active_health_issues()

    def eat(self):
        return f"{self.__name} eats {self.__diet}"

    def sleep(self):
        return f"{self.__name} is sleeping"

    def make_sound(self):
        return f"{self.__name} makes a sound"

    def __str__(self):
        display_status = "On display" if self.__on_display else "not on display"
        health_status = "unwell" if self.__active_health_issues() else "healthy"
        return f"{self.__name} ({self.__species}, {self.__age} years) | {display_status}, {health_status}"


class Healthissue:

    def __init__(self, description, severity, treatment):
        self.__description = description
        self.__severity = severity
        self.__treatment = treatment
        self.__resolved = False
        self.__notes = ""


    def get_description(self):
        return self.__description

    def get_severity(self):
        return self.__severity

    def get_treatment(self):
        return self.__treatment

    def get_resolved(self):
        return self.__resolved

    def get_notes(self):
        return self.__notes

    def mark_resolved(self, notes=""):
        self.__resolved = True
        self.__notes = notes

    def __str__(self):
        status = "resolved" if self.__resolved else "Active"
        return f"[{status}] {self.__description} (Severity: {self.__severity})"

class Mammal(Animal):
    def __init__(self, name, species, age, diet, environment_type):
        super().__init__(name, species, age, diet, environment_type)
        self.__category = "Mammal"

    def get_category(self):
        return self.__category

    def make_sound(self):
        return f"{self.__get_name()} makes a mammal sound"

class Bird(Animal):
    def __init__(self, name, species, age, diet, environment_type):
        super().__init__(name, species, age, diet, environment_type)
        self.__category = "Bird"




