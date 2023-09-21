# this class violates the SRP guide because the same class that prints/displays the sound is the same that displays
# the animal's name and its feeding type. To fix this, the Sound amd the feeding types properties with their display
# methods should be on their own classes from the Animal class

class Animal:
    # constructor
    def __init__(self, name, sound, feeding_type="omnivorous"):
        self.name = name
        self.sound = sound
        self.feeding = feeding_type

    # sets animal's name
    def setName(self, name):
        self.name = name

    # sets animal's sound made
    def setSound(self, sound_made):
        self.sound = sound_made

    # sets animal's feeding type
    def setFeedingType(self, feeding):
        self.feeding = feeding

    # returns the Animal's name
    def getName(self):
        return self.name

    # returns the sound produces
    def getSound(self):
        return self.sound

    # returns the feeding type
    def getFeedingType(self):
        return self.feeding

    # displays/prints the animal name
    def printName(self):
        print(f"I belong to the Animal class and my name is {self.name}")

    # displays/prints the sound produced by the animal
    def printSound(self):
        print(f"I make the {self.sound} sound.")

    # displays/prints the feeding type
    def printFeedingType(self):
        print(f"I am {self.feeding}.")


if __name__ == "__main__":
    # animal object 1
    animal1 = Animal("Lion", "roars", "carnivorous")
    animal1.printName()  # I belong to the Animal class and my name is Lion
    animal1.printSound()  # I make the roars sound.
    animal1.printFeedingType()  # I am carnivorous.

    print()
    # Animal Object 2
    animal2 = Animal("Wildebeest", "moans/snorts")
    animal2.setFeedingType("Herbivorous")  # set the feeding type for animal 2
    animal2.printName()  # I belong to the Animal class and my name is Wildebeest
    animal2.printSound()  # I make the moans/snorts sound.
    animal2.printFeedingType()  # I am herbivorous.
