## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

      def __init__(self, name):
          ## Person has-a name
          self.name = name

          ## Person has-a pet of some kind
          self.pet = None



## Person is-a Employee
class Employee(Person):

    def __init__(self, name, salary):
        ## Person has-a self name and salary in super class
        super (Employee, self).__init__(name)
        ## salary has-a salary ?
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")


## satan is-a cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## Mary has-a pet
mary.pet = satan

## Frank is-a employee with salary 120000
frank = Employee("Frank", 120000)

## Frank has-a pet rover
frank.pet = rover

## Flipper is-a fish
flipper = Fish()

## Salmon is-a crouse
crouse = Salmon()

## Harry is-a halibut
harry = Halibut()
