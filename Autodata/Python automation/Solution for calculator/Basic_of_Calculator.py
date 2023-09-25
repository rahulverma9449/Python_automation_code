"""
Create a class that has basic calculating functions.

You can have as many methods as you like but here are few suggestions.
* method to taake two numbers and add them and return the sum.
* method to take two numbers and subtract the second number from the first number.
* method to take two numbers and return the multiplication of the two.
* method to divide two numbers and retrun the result(first number divided both numbers)

"""
class BasicCalculatorV2:

    def __init__(self, x ,y):
        self.x = x
        self.y = y


    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y
    def multiply(self):
        return self.x * self.y

    def devide(self):
        return self.x/self.y



mycalc = BasicCalculatorV2(12,10)
my_sum = mycalc.add()
print(my_sum)
print(mycalc.subtract())
print(mycalc.multiply())
