'''
OOP is a way of organizing code using Classes and Objects.
'''
#Class: is a blueprint for creating objects.
#class is called automatically when obj is created
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
#All classes have a built-in constructor called __init__(), which is always executed when the class is being initiated.
#The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
#self keyword refers to the current object.
class Student:
    def __init__(self, name):#executed when class is invoked
        self.name = name
        print('Welcome',self.name)#self refere to current object i.e s1

s1 = Student("Chay")

print(s1.name)

#methods: its a function inside a class,runs only when called.
#instance method: uses self 
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

#static method: doesnt takes self parameter by using  a decorator over that method
class hello:
  @staticmethod
  def greet():
    print('hi')

s1=hello()
s1.greet()#without static returns TypeError: hello.greet() takes 0 positional arguments but 1 was given
#bcz of object invokes,if invoke from class directly it works like hello.greet()

#class method:used to work with class variables and uses cls
class Cse:
  section = 'C'
  print(section,'Before set')
  @classmethod
  def set_sec(cls,sec):
    cls.section = sec#or without dec you can use self.__class__.section=sec
    print(cls.section,'After set')

cls=Cse()
cls.set_sec('D')


