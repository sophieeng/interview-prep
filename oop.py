from math import pi

# Class and object
class Shape: 
    # class attribute
    dimensions = 2

    def __init__(self, name):
        self.name = name # instance attribute

    def area(self):
        pass

    def fact(self):
        return "I am a geometric shape"

    def __str__(self):
        return self.name

print("======== Class and Object ========")
shape1 = Shape("rectangle")
print(shape1)
print(f"shape1 is a {shape1.name}")
print(shape1.fact())
print(f"I have this many dimensions: {shape1.dimensions}")

# Inheritance

# create new class with details of existing class
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle") # super() means it searches the parent class for the method
        self.radius = radius

    def area(self):
        return pi*(self.radius**2)

print("\n======== Inheritance ========")
shape2 = Circle(3)
print(shape2)
print(shape2.area())
print(shape2.fact()) # using the fact method from Shape class
    
# Encapsulation

# bundle attributes within class
# use private attributes
class Triangle(Shape):
    def __init__(self, height):
        super().__init__("Triangle")
        self.height = height
        self.__base = 5

    def area(self):
        return (self.height * self.__base)/2

    def base(self, base):
        self.__base = base

print("\n======== Encapsulation ========")
shape3 = Triangle(6)
print(shape3.area())
shape3.__base = 7
print(shape3.area())
shape3.base(7)
print(shape3.area())

# Polymorphism

# have classes with the same method names
class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    # method overriding
    def fact(self):
        return "All my sides are the same length"

print("\n======== Polymorphism ========")
shape4 = Square(3)
print(shape4)
print(shape4.area())
print(shape4.fact())

print(isinstance(shape4, Square))
print(isinstance(shape4, Triangle))
print(isinstance(shape4, Shape))