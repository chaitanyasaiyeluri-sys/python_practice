a = 10
b = 3

# Arithmetic Operators - Perform mathematical calculations
print("Arithmetic Operators:")
# + : Adds two values
print("Addition:", a + b)
# - : Subtracts right value from left
print("Subtraction:", a - b)
# * : Multiplies two values
print("Multiplication:", a * b)
# / : Returns division result as float
print("Division:", a / b)
# // : Returns integer quotient
print("Floor Division:", a // b)
# % : Returns remainder
print("Modulus:", a % b)
# ** : Raises to a power
print("Exponentiation:", a ** b)

# Comparison Operators - Compare two values and return True or False
print("\nComparision Operators:")
# == : Checks if values are equal
print("Equal To:", a == b)
# != : Checks if values are not equal
print("Not Equal To:", a != b)
# > : Checks if left value is greater
print("Greater Than:", a > b)
# < : Checks if left value is smaller
print("Less Than:", a < b)
# >= : Checks if left value is greater or equal
print("Greater Than or Equal To:", a >= b)
# <= : Checks if left value is less or equal
print("Less Than or Equal To:", a <= b)

# Assignment Operators - Assign or update variable values
print("\nAssignment Operators:")
x = 10
# = : Assigns a value
print("Assignment:", x)
# += : Adds and assigns
x += 5
print("Add and Assign:", x)
# -= : Subtracts and assigns
x -= 2
print("Subtract and Assign:", x)
# *= : Multiplies and assigns
x *= 2
print("Multiply and Assign:", x)
# /= : Divides and assigns
x /= 2
print("Divide and Assign:", x)
# //= : Floor divides and assigns
x //= 2
print("Floor Divide and Assign:", x)
# %= : Finds remainder and assigns
x %= 2
print("Modulus and Assign:", x)
# **= : Raises power and assigns
x = 2
x **= 3
print("Power and Assign:", x)

# Logical Operators - Combine or reverse Boolean values
print('\nLogical Operators:')
# and : True if both conditions are True
print("AND:", True and False)

# or : True if at least one condition is True
print("OR:", True or False)

# not : Reverses a Boolean value
print("NOT:", not True)


# Bitwise Operators - Operate on binary representations of numbers
print("\nBitwise Operators:")
# & : Bitwise AND
print("Bitwise AND:", 5 & 3)

# | : Bitwise OR
print("Bitwise OR:", 5 | 3)

# ^ : Bitwise XOR
print("Bitwise XOR:", 5 ^ 3)

# ~ : Bitwise NOT
print("Bitwise NOT:", ~5)

# << : Left shift bits
print("Left Shift:", 5 << 1)

# >> : Right shift bits
print("Right Shift:", 5 >> 1)


# Membership Operators - Check whether a value exists in a collection
print("\nMembership Operators:")
numbers = [1, 2, 3, 4, 5]

# in : Checks if value exists
print("In:", 3 in numbers)

# not in : Checks if value does not exist
print("Not In:", 10 not in numbers)


# Identity Operators - Check whether two variables refer to the same object
print("\nIdentity Operators:")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

# is : Checks if both refer to the same object
print("Is:", list1 is list2)

# is not : Checks if objects are different
print("Is Not:", list1 is not list3)

# Walrus Operator - Assigns a value inside an expression
print("\nWalrus Operator:")
# := : Assigns and returns the value
if (length := len("Python")) > 5:
    print("Length of PYTHON:", length)

''' precedence of operators
in case of same precedence ,evaluates from left
exception in exponential ** evaluates from right

()
**
+x  -x
*  /  //  %
+  -
<< >>
&
^
|
Comparisons
not
and
or
Assignment
'''

