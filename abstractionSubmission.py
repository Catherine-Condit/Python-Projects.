from abc import ABC, abstractmethod

class Employee(ABC):
    #define regular method with implementation
    def work(self):
        print("I am a {}.".format(self.__class__.job_title)) #adds specific job title case by case
    
    #define abstract method without implementation yet
    @abstractmethod
    def role(self):
        pass
    
    #define regular method with implementation
    def department(self):
        print("As an employee I work in the {} department.".format(self.__class__.department_name))

class Manager(Employee):
    job_title = "Mananger"
    department_name = "Management"
    
    def role(self):
        #implement abstract method from parent class
        print("I oversee the team and make strategic decisions.")

class Developer(Employee):
    job_title = "Developer"
    department_name = "Development"
    
    def role(self):
        #implement abstract method from parent class
        print("I write and maintain code for the company's systems.")

class Designer(Employee):
    job_title = "Designer"
    department_name = "Design"
    
    def role(self):
        #implement abstract method from parent class
        print("I design user-friendly interfaces and experiences.")

if __name__ == "__main__":
    #create objects of the child classes
    manager = Manager()
    developer = Developer()
    designer = Designer()
    
    #call the abstract method by the child class and regular methods
    print("Manager:")
    manager.work()  #calls regular method from Employee class
    manager.role()  #calls implemented method from Manager class
    manager.department()  #calls regular method from Employee class
    
    print("\nDeveloper:")
    developer.work()  #calls regular method from Employee class
    developer.role()  #calls implemented method from Developer class
    developer.department()  #calls regular method from Employee class
    
    print("\nDesigner:")
    designer.work()  #calls regular method from Employee class
    designer.role()  #calls implemented method from Designer class
    designer.department()  #calls regular method from Employee class
