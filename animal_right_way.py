# correct Animal class that meets the SRP guidelines
# Every class does its own task, one defines the animal, the other deals with the sound and lastly, the feeding type
class Animal:
    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def printName(self):
        print(f"I am {self.name}.")


class Sound:
    def __init__(self, animalOBJ, sound_made):
        self.animal = animalOBJ
        self.sound = sound_made

    def setSound(self, sound):
        self.sound = sound

    def getSound(self):
        return self.sound

    def printSound(self):
        print(f"I am {self.animal.name} and I give the {self.sound} sound.")


class FeedingType:
    def __init__(self, animalOBJ, feeding_type=""):
        self.animal = animalOBJ
        self.feeding = feeding_type

    def setFeedingType(self, feeding):
        self.feeding = feeding

    def getFeedingType(self):
        return self.feeding

    def printFeedingType(self):
        print(f"I am {self.animal.name} and I am {self.feeding}.")


if __name__ == "__main__":
    # animal 1 object
    animal1 = Animal("Lion")
    animal1Sound = Sound(animal1, "roars")
    animal1Feeding = FeedingType(animal1, "carnivorous")

    animal1.printName()  # I am Lion.
    animal1Sound.printSound()  # I am Lion and I give the roars sound.
    animal1Feeding.printFeedingType()  # I am Lion and I am carnivorous.

    # animal 2 object
    animal2 = Animal("Wildebeest")
    animal2Sound = Sound(animal2, "snorts")
    animal2Feeding = FeedingType(animal2, "herbivorous")

    print()
    animal2.printName()  # I am Wildebeest.
    animal2Sound.printSound()  # I am Wildebeest and I give the snorts sound.
    animal2Feeding.printFeedingType()  # I am Wildebeest and I am herbivorous.
