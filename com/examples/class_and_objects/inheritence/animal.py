class Animal:
    name = ""
    animal_type = ""
    __var_private = "This is private Variable"

    #private methods - These methods are accesible with in the class. No access to outsiders
    def __test_private(self):
        print("It is private method and it won't be accessed from outside.")

    #protected methods(double '__')  - Only childs can access these methods/variable. No access to outsiders

    def make_sound(self):
        print("Making sound.")

    def print_animal_name(self):
        print("Animal name is ", self.name)

    def print_animal_type(self):
        print("Animal type is ", self.animal_type)


class Cat(Animal):
    name = "Cat"
    animal_type = "Not a wild Animal"

    def make_sound(self):
        print("Miaaaw..")

class Tiger(Animal):
    name = "Tiger"
    animal_type = "Wild Animal"

    def make_sound(self):
        print("AAaaaaa")

class Tortoise(Animal):
    name = "Tortoise"
    animal_type = "Mammal"

    def make_sound(self):
        print("sssssss")


class Ant(Animal):
    name = "Ant"


cat = Cat()
cat.make_sound()


tiger = Tiger()
tiger.make_sound()

tortoise = Tortoise()
tortoise.make_sound()

ant = Ant()
ant.make_sound()

