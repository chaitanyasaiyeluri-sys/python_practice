'''
OOP is a way of organizing code using Classes and Objects.

'''
#Class: is a blueprint/template for creating objects.
#Pascal case is used for naming like class WelcomeToClass:
#you can also use () after class name

#Object: is an instance of a class

class MyClass:#this is a class
  x = 5

p1 = MyClass() #this is a object created from the class
print(p1.x)

print(MyClass)
print(p1)
a=MyClass()
#delete keyword: del is used for deleting objects,obj properties,class references
del MyClass

print(p1)
print(a)
#print(MyClass)

#Constructor: is a special method that runs automatically when an object is created.
#All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
#The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
#self keyword refers to the current object.
class Student:
    def __init__(self, name):#executed when class is invoked
        self.name = name
        print('Welcome',self.name)#self refere to current object i.e s1

s1 = Student("Chay")

print(s1.name)

#methods
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Chay")
p1.greet()

#method with parameters:
class Calculator:
  def add(self, a, b):
    return a + b
  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

