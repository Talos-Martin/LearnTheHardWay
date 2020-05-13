#Animal is an object
class Animal(object):
    def stuff(self, color):
        self.color = color

#Class Dog is an animal!?
class Dog(Animal):
    def __init__(self,name):
        #sets the class variable name to the supplied parameter 'name'
        self.name = name
        self.test = "Test"

#Animal. Named Cat.
class Cat(Animal):
    def __init__(self, name):
        #see Dog
        self.name = name
        super(Cat, self).stuff("blue")  ## all animals are blue right?


# Person is an object
class Person(object):
    def __init__(self, name):
        self.name = name
        # Person may have an animal. Here, it doesn't
        self.pet = None     # None seems to be a keyword. Kinda like NULL in C I guess

#Employee is a Person.
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)    #calls the init function of the parent class, which is Person, and sets the variable name to parameter 'name'
        self.salary = salary




class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass


rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")
mary.pet = satan

#instantiate class Employee Object with a person named Frank and his 120.000 salary
frank = Employee("Frank", 120000)

#set variable pet in class frank to the object rover of class dog/animal
frank.pet = rover

#class object. Instantiation of Fish() and assigned to variable flipper
flipper = Fish()

crouse = Salmon()

harry = Halibut()



