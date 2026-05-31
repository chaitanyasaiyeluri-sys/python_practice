"""
List is a data type which stores a set of items
similar to arrays but it can store items are different types
Lists are mutable
allows duplicates
syntax:
list_name=[item1,"item2",itemn]
"""
# Creating Lists - Store multiple values
numbers = [10, 20, 30, 40, 50]

print("\n--- Original List ---")
print(numbers)

# len() - Returns number of elements
print("\n--- Length of List ---")
print(len(numbers))

# Positive Indexing - Access element by position
print("\n--- Positive Indexing ---")
print('Num at 0 :',numbers[0])   # First element
print('Num at 2 :',numbers[2])   # Third element

# Negative Indexing - Access from end
print("\n--- Negative Indexing ---")
print('Num at -1 :',numbers[-1])  # Last element
print('Num at -2 :',numbers[-2])  # Second last element

# Slicing - Extract part of list
print("\n--- List Slicing ---")
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

# Reverse List using Slicing
print("\n--- Reverse List ---")
print(numbers[::-1])

# Modify Element
print("\n--- Modify Element ---")
numbers[1] = 25
print(numbers)

# append() - Add element at end
print("\n--- append() ---")
numbers.append(60)
numbers.append(25)
print(numbers)

# insert() - Add element at specific index
print("\n--- insert() ---")
numbers.insert(1, 15)#(index,element)
print(numbers)

# remove() -Removes first matching value
print("\n--- remove() ---")
numbers.remove(25)
print(numbers)

# pop() - Remove element by index
print("\n--- pop() ---")
numbers.pop(0)
print(numbers)

# Membership Operators
print("\n--- Membership Operators ---")
print(30 in numbers)
print(100 not in numbers)

# Loop Through List
print("\n--- Loop Through List ---")
for num in numbers:
    print(num,end=" ")

# sort() - Sort ascending
print("\n--- sort() ---")
numbers.sort()
print(numbers)

# reverse() - Reverse current order
print("\n--- reverse() ---")
numbers.reverse()
print(numbers)

# count() - Count occurrences
print("\n--- count() ---")
print(numbers.count(30))

# index() - Find position of element
print("\n--- index() ---")
print(numbers.index(30))

# copy() - Create separate copy
print("\n--- copy() ---")
new_list = numbers.copy()
print(new_list)

# Concatenation - Combine lists
print("\n--- List Concatenation ---")
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)

# Repetition - Repeat list
print("\n--- List Repetition ---")
print([1, 2] * 3)

# Useful Functions
print("\n--- Useful Functions ---")
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# Nested List (2D List)
print("\n--- Nested List (2D List) ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[1][2])


# List Comprehension
print("\n--- List Comprehension ---")
squares = [x * x for x in range(1,5)]
print(squares)

# clear() - Remove all elements
print("\n--- clear() ---")
numbers.clear()
print(numbers)