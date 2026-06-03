'''A set is an unordered collection of unique elements.
Key Properties:
Unordered 
Mutable 
No Indexing 
No Slicing 
Uses Curly Braces {}
'''

# Creating Sets
numbers = {10, 20, 30, 40, 50}

print("\n--- Original Set ---")
print(numbers)

# len() - Returns number of elements
print("\n--- Length ---")
print(len(numbers))

# add() - Add a single element
print("\n--- add() ---")
numbers.add(60)
print(numbers)

# update() - Add multiple elements
print("\n--- update() ---")
numbers.update([70, 80])
print(numbers)

# remove() - Remove element (Error if not found)
print("\n--- remove() ---")
numbers.remove(20)
print(numbers)

# discard() - Remove element (No Error if not found)
print("\n--- discard() ---")
numbers.discard(100)
print(numbers)

# pop() - Remove random element
print("\n--- pop() ---")
removed = numbers.pop()
print("Removed:", removed)
print(numbers)

# copy() - Create copy
print("\n--- copy() ---")
new_set = numbers.copy()
print(new_set)

# clear() - Remove all elements
print("\n--- clear() ---")
temp = numbers.copy()
temp.clear()
print(temp)