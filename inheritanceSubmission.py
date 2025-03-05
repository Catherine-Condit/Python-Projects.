class People: #created parent class
    def __init__ (self, name, gender):
        self.name = name
        self.gender = gender

    def describe(self):
            return f"This is a {self.gender} named {self.name}."

class Male(People): #created child class
    def __init__ (self, name, gender, job, age): #each child has at least two of their own attributes
        super().__init__(name, gender)
        self.job = job
        self.age = age

    def display_info(self):
        return f"{self.name} is a {self.age} year old {self.job}."


class Female(People): #created child class
    def __init__ (self, name, gender, job, age): #each child has at least two of their own attributes
        super().__init__(name, gender)
        self.job = job
        self.age = age

    def display_info(self):
        return f"{self.name} is a {self.age} year old {self.job}."


if __name__ == "__main__":
    male = Male("Joe", "Male", "Construction Worker", 35)
    print(male.describe())
    print(male.display_info())

    female = Female("Susan", "Female", "Hairstylist", 25)
    print(female.describe())
    print(female.display_info())
    

        
