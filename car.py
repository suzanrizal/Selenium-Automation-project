# Class car and its methods 

# class car:
#     def __init__(self, brand, color):
#         self.brand = brand   
#         self.color = color

#     def print_brand(self):
#         print("Car brand is: ", self.brand)

#     def print_color(self):
#         print("Car color is: ", self.color)

# car1 = car("Toyota","Red")
# car1.print_brand()
# car1.print_color()


# Calculator

class calculator:
    def add(self, a, b):
        print(a+b)

    def subtract(self, a, b):
        print(a-b)

    def multiply(self, a, b):
        print(a*b)

obj = calculator()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
obj.add(10,5)
obj.subtract(10,5)
obj.multiply(10,5)
        