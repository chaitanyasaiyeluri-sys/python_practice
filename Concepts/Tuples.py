'''
A tuple is an ordered collection of items, similar to a list, but immutable (cannot be modified after creation)
Ordered 
Immutable (Can't directly changed)
Allows duplicates
Supports indexing and slicing
Uses parentheses () 
'''

# Creating Tuples
numbers = (10, 20, 30, 40, 50)

print("\n--- Original Tuple ---")
print(numbers)

# len() - Returns number of elements
print("\n--- Length of Tuple ---")
print(len(numbers))

# Positive Indexing
print("\n--- Positive Indexing ---")
print(numbers[0])
print(numbers[2])

# Negative Indexing
print("\n--- Negative Indexing ---")
print(numbers[-1])
print(numbers[-2])

# Slicing
print("\n--- Tuple Slicing ---")
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

# Reverse Tuple
print("\n--- Reverse Tuple ---")
print(numbers[::-1])

# Membership Operators
print("\n--- Membership Operators ---")
print(30 in numbers)
print(100 not in numbers)

# Loop Through Tuple
print("\n--- Loop Through Tuple ---")
for num in numbers:
    print(num)

# count() - Counts occurrences
print("\n--- count() ---")
print(numbers.count(30))

# index() - Finds position
print("\n--- index() ---")
print(numbers.index(40))

# Concatenation
print("\n--- Tuple Concatenation ---")
tuple1 = (1, 2)
tuple2 = (3, 4)
print(tuple1 + tuple2)

# Repetition
print("\n--- Tuple Repetition ---")
print((1, 2) * 3)

# Useful Functions
print("\n--- Useful Functions ---")
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# Tuple Packing
print("\n--- Tuple Packing ---")
person = ("Sai", 20, "Python")
print(person)

# Tuple Unpacking
print("\n--- Tuple Unpacking ---")
name, age, course = person
print(name)
print(age)
print(course)

# Single Element Tuple
print("\n--- Single Element Tuple ---")
single = (10,)
print(type(single))

# Nested Tuple
print("\n--- Nested Tuple ---")
data = (
    (1, 2),
    (3, 4)
)
print(data[1][0])