'''
A function is a reusable block of code that performs a specific task.
def keyword is used to define a function
#defining a function
def f_name(): #()holds parameters to take input
    pass
    
#calling a function
f_name() #()holds arguments the actual value of the parameters
'''
# Built-in Functions
print("Hello")
print(len("Python"))

# User-defined Function
# created by using 'def'
def greet():
    print("Hello Python")
greet()

# Function with Parameters
# Parameters receive values when the function is called.
def greet(name):
    print("Hello", name)
greet("Sai")

# Function with Return Value
# return sends a value back to the caller.

def add(a, b):
    return a + b
result = add(10, 20)
print(result)

# Default Parameter
# Uses a default value if no argument is provided.
def greet(name="Guest"):
    print("Hello", name)
greet()
greet("Sai")

# Keyword Arguments
# Pass arguments using parameter names.
def student(name, age):
    print(name, age)

student(age=20, name="Sai")

# *args: Accepts any number of positional arguments.
# Stored as a tuple.
def total(*numbers):
    print(numbers)
total(10, 20, 30, 40)

# **kwargs: Accepts any number of keyword arguments.
# Stored as a dictionary
def info(**data):
    print(data)

info(name="Sai", age=20)


# Lambda Function: Small anonymous one-line function.
#lambda parameters:expression
square = lambda x: x * x
print(square(5))

# Recursive Function
# Function that calls itself.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Local Variable: created inside a function.
# Accessible only inside that function.
def demo():
    x = 10
    print(x)
demo()

# Global Variable: created outside functions.
# Accessible throughout the program.
x = 100
def show():
    print(x)

show()


# Function Returning Multiple Values
# Multiple values are returned as a tuple.
def values():
    return 10, 20, 30
a, b, c = values()
print(a, b, c)


# Nested Function
def outer():

    def inner():
        print("Inner Function")

    inner()

outer()