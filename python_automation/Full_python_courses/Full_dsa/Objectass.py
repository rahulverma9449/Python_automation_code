# class Circle(object):
#
#     def __init__(self, radius):
#         self.__radius = radius
#
#     def __str__(self):
#         return "this is a circle class which takes radius as ab argument."
#
# c = Circle(3)
# print(c)

# Parent Class
class vehicle():

    def __init__(self, make,model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel
# Child Class
class Car(vehicle):
    def __init__(self, make, model, fuel, air_conditioning, sunroof):

        super(Car, self).__init__(make, model, fuel)

        self._air_conditioning = air_conditioning
        self.__sunroof = sunroof
class ElectricVehicle(Car):
    def __init__(self,make, model, fuel, air_conditioning, sunroof, distance):

        self.distance = distance

myobj = ElectricVehicle("tesla",2019, "Electric",True,True,500)
myobj.__dict__

