

class Car:
    def __init__(self, make, model, year):
        # private attribute (cannot be accessed directly outside the class)
        self.__make = make
        # protected attribute (should not be accessed directly outside the class)
        self._model = model
        # protected attribute for year
        self._year = year
        print(self.__make)
        
    # private method (cannot be accessed directly outside the class)
    def __display_info(self):
        return f"{self._year} {self._model}"

    # public method to start the car
    def start(self):
        print(f"The {self.__make} {self.__display_info()} is now running.")

    # public method to stop the car
    def stop(self):
        print(f"The {self.__make} {self.__display_info()} has stoppped.")


#main block where the class is used
if __name__ == "__main__":
    #creating an object of the Car class
    car = Car("Toyota", "Corolla", 2020)
    #start and stop the car using public methods
    car.start()
    car.stop()

    #accessing protected attributes directly (not recommended)
    print(f"Car model: {car._year} {car._model}")

    #accessing private method (not recommended, this will cause an error)
    #print(car.__display_info())
    #this will raise an AttributeError since __display_info is private

    
