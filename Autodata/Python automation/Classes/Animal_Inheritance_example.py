import pdb


class Animal:

    def __init__(self, color, food_type):
        print("I am init.")
        self.color = color
        self.food_type = food_type

    def move(self):
        print("Animal moves")

    def eat(self):
        print("Animal eat")
        print("This animal eats {}".format(self.food_type))

    def breath(self):
        print("Animal breath")
    def mian(self):
        self.move()
        self.eat()
        self.breath()


my_animal1 = Animal('blue', 'meat')
print(f" color of animal 1: {my_animal1.color}")

my_animal1.mian()
# my_animal1.move()
# my_animal1.eat()
# my_animal1.breath()
# print(my_animal1.move)

# my_animal2 = Animal('red', 'chips')
# my_animal2.eat()
# print(f" color of animal 2: {my_animal2.color}")
#
# my_animal3 = Animal('orange', ' veg')
# print(f" color of animal 3: {my_animal3.color}")
# print(my_animal1)
# print(my_animal2)
# print(my_animal3)
# pdb.set_trace()
#


class Dog(Animal):

    def __init__(self, color, food_type,  breed, name):
        super().__init__(color,food_type)
        self.dog_breed = breed
        self.dog_name = name

    # def eat(self):
    #     print("eat.....")

    def bark(self):
        print("wooff")

    # def breath(self):
    #     print("breath....")


    def as_security(self):
        print("My dog is my home security")


class Cat(Animal):

    def __init__(self, color, food_type, breed, name):
        super().__init__(color, food_type)
        self.cat_breed = breed
        self.act_name = name

    # def eat(self):
    #     print("Eat......")

    def meaw(self):
        print("Meawwww")

mydog = Dog("Brown", "Meat", "Bulldog", "Max")
print(mydog.dog_breed)
print(mydog.dog_name)
mydog.eat()

mycat = Cat("Red","Rat","jungle","darkcat")
mycat.eat()
mycat.meaw()