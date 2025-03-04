

class Animal: #parent class
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self): #parent class method
        return f"{self.name} makes a sound." #provides meaningful default msg, but doesn't overcomplicate things


class Dog(Animal): #first child class
    def __init__(self, name, breed, age):
        super().__init__(name, "Dog") #Calling parent constructor
        self.breed = breed
        self.age = age

    def speak(self): #overriding 'speak' method to be more specific
        return f"{self.name} barks!"

class Cat(Animal): #second child class
    def __init__(self, name, color, is_indoor):
        super().__init__(name, "Cat")  # Calling parent constructor
        self.color = color
        self.is_indoor = is_indoor

    def speak(self):  #overriding 'speak' method to be more specific
        return f"{self.name} meows softly!"

if __name__ == "__main__":
    dog = Dog("Seamus", "Terrier", 5) #create instances
    cat = Cat("Percy", "Gray", True)

    print(dog.speak()) #print!
    print(cat.speak())
