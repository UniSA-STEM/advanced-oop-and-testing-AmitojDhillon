'''
File: main.py
Description: A brief description of this Python module.
Author: Amitoj Dhillon
ID: 110408872
Username: Dhiay010
This is my own work as defined by the University's Academic Integrity Policy.
'''


from animal import Mammal, Bird, Reptile
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian


leo = Mammal("Leo", "Lion", 6, "meat", "savannah")
zara = Mammal("Zara", "Lion", 3, "meat", "savannah")
rio = Bird("Rio", "Parrot", 4, "seeds", "aviary")
luna = Bird("Luna", "Parrot", 1, "seeds", "aviary")
fang = Reptile("Fang", "Python", 9, "rodents", "rainforest")
ember = Reptile("Ember", "Python", 5, "meat", "rainforest")

all_animals = [leo, zara, rio, luna, fang, ember]

print("Animals Created:")
for a in all_animals:
    print(" -", a)
print()

savannah = Enclosure("Savannah Habitat", 500, "savannah", 3, "Lion")
aviary = Enclosure("Aviary", 200, "aviary", 4, "Parrot")
rainforest = Enclosure("Rainforest Exhibit", 300, "rainforest", 3, "Python")

enclosures = [savannah, aviary, rainforest]

print("Enclosures Created:")
for e in enclosures:
    print(" -", e)
print()

savannah.add_animal(leo)
savannah.add_animal(zara)
aviary.add_animal(rio)
aviary.add_animal(luna)
rainforest.add_animal(fang)
rainforest.add_animal(ember)

print("Animals Added to Enclosures:")
for e in enclosures:
    print(" -", e)
print()

keeper = Zookeeper("Amy", "ZK001")
vet = Veterinarian("Dr. Ben", "VT101")

for e in enclosures:
    keeper.assign_enclosure(e)

print("Staff Members:")
print(" -", keeper.get_summary())
print(" -", vet.get_summary())
print()

print("Daily Feeding Routine:")
print(" ->", keeper.feed_animal(leo))
print(" ->", keeper.feed_animal(rio))
print(" ->", keeper.feed_animal(fang))
print()

print("Cleaning Routine:")
for e in enclosures:
    print(" ->", keeper.clean_enclosure(e))
print()

print("Veterinarian Recording Health Issue:")
vet.record_health_issue(leo, "Limping front leg", "Moderate", "Rest and medication")

print("Leo Health Issues:")
for issue in leo.get_health_issues():
    print(" ->", issue)
print()

leo.set_on_display(True)
print("Leo Display Status:", leo.get_on_display())
print()

print(vet.resolve_all_issues(leo, "Responded well to treatment"))
print()

leo.set_on_display(True)
print("Leo Display Status After Recovery:", leo.get_on_display())
print()

savannah.remove_animal(zara)
print("Zara Removed From Savannah Enclosure")
print("Updated Savannah:", savannah)
print()

print("Animals by Species:")
species_map = {}
for animal in all_animals:
    species_map.setdefault(animal.get_species(), []).append(animal.get_name())

for species, names in species_map.items():
    print(f" - {species}: {', '.join(names)}")
print()

print("Enclosure Reports:")
for e in enclosures:
    print(" -", e)
print()

print("Animal Health Reports:")
for animal in all_animals:
    print(f"{animal.get_name()}:", end=" ")
    if animal.get_health_issues():
        for issue in animal.get_health_issues():
            print(issue)
    else:
        print("No health issues")
print()

