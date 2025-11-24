'''
File: filename.py
Description: A brief description of this Python module.
Author: Amitoj Dhillon
ID: 110100110
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
