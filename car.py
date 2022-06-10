class Vehicle:
     color="white"
     def __init__(self,name,max_speed,mileage):
         self.name=name
         self.max_speed=max_speed
         self.mileage=mileage

     def congz(self,owner):
         self.owner=owner
         return f"Hello {owner}, Congratulations for buying {self.color} {self.name} car with the maximum speed of {self.max_speed}, and {self.mileage} mileage."

     def cap(self,capacity):
         self.capacity=capacity
         return f"This {self.name} car has the capacity to carry{capacity} people"



    #Object Oriented Programming Python

#1a) Create a class Vehicle with the following attributes:name, max_speed,mileage. Define attribute color to be “White” for all the vehicles.
 #Create two instances to confirm it works.
#b) Create a method that congratulates the owner  for buying that kind of a car. Include the car’s name, color,max_speed,mileage.
#c)Create a method that returns the car name and its capacity.
