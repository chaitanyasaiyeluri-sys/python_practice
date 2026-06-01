'''
A dictionary stores data as key:value pairs.
Key Properties:
Mutable 
Ordered (Python 3.7+) 
Key-Value Pairs 
Duplicate Keys Not Allowed 
Duplicate Values Allowed 
Uses Curly Braces {} 
'''
# Creating Dictionary
student = {
    "name": "Sai",
    "age": 20,
    "course": ["Python","java"]
}

print("\n--- Original Dictionary ---")
print(student)

# Access Value by Key
print("\n--- Access Values ---")
print(student["name"])
print(student["age"])

# get() - Safely access value
print("\n--- get() ---")
print(student.get("course"))

# Add New Key-Value Pair
print("\n--- Add Item ---")
student["city"] = "Hyderabad"
print(student)

# Update Existing Value
print("\n--- Update Item ---")
student["age"] = 21
print(student)

# len() - Number of key-value pairs
print("\n--- Length ---")
print(len(student))

# keys() - Returns all keys
print("\n--- keys() ---")
print(student.keys())

# values() - Returns all values
print("\n--- values() ---")
print(student.values())

# items() - Returns key-value pairs
print("\n--- items() ---")
print(student.items())

# Check Key Exists
print("\n--- Membership ---")
print("name" in student)
print("salary" not in student)

# Loop Through Keys
print("\n--- Loop Keys ---")
for key in student:
    print(key)

# Loop Through Values
print("\n--- Loop Values ---")
for value in student.values():
    print(value)

# Loop Through Key-Value Pairs
print("\n--- Loop Items ---")
for key, value in student.items():
    print(key, ":", value)

# pop() - Remove by key
print("\n--- pop() ---")
student.pop("city")
print(student)

# popitem() - Remove last item
print("\n--- popitem() ---")
student.popitem()
print(student)

# update() - Add/Update multiple items
print("\n--- update() ---")
student.update({"city": "Hyderabad", "grade": "A"})
print(student)

# copy() - Create copy
print("\n--- copy() ---")
new_student = student.copy()
print(new_student)

# clear() - Remove all items
print("\n--- clear() ---")
temp = student.copy()
temp.clear()
print(temp)