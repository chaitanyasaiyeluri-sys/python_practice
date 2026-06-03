'''String is a data type which stores sequence of characters.
strings can be enclosed by " " or ' ' or ''' ''' or """ """
Strings are immutable 
Escape sequences are special character combinations that start with a backslash \
They are used to represent characters that are difficult to type directly.
| Escape Sequence | Meaning      |
| --------------- | ------------ |
| `\n`            | New line     |
| `\t`            | Tab space    |
| `\\`            | Backslash    |
| `\'`            | Single quote |
| `\"`            | Double quote |
'''
#Operations on strings
#Concatenation
print('Concatenation of Num & bers:','Num'+'bers')#Numbers

#length of the string. All characters are considered in len including a space
print('Length of Apple is:',len('apple'))#5

#indexing: by using indexing we can access specific character/s of string
#but we can can't edit strings using indexing
#index value starts from 0
name="Chaitanya"
print('Char at index 0 is:',name[0])#C

#slicing: accessing parts of string
#syntax: string[ starting_index : ending_index ] #ending index is not included
print('Slicing:')
print(name[0:4])
print(name[:4])#same as [0:5]
print(name[0:])#same as [0:len(string)],to print whole string

#negative indexing
#here -1 will the last position of the string
#and the starting position will be -len(string)-1
print(name[-1:-len(name)-1:-1])
print(name[::-1])#same as above

text = "python programming"
# Repetition - Repeat string
print("Hi " * 3)

# Membership Operators
print("Py" in name)
print("Java" not in name)

# Case Conversion Methods
print(text.upper())      # Uppercase
print(text.lower())      # Lowercase
print(text.capitalize()) # First letter uppercase
print(text.title())      # First letter of each word uppercase

# Search Methods
print(text.find("pro"))  # Find position
print(text.count("m"))   # Count occurrences

# Replace Method
print(text.replace("python", "Java"))

# Split Method - String to List
print("Python,Java,C".split(","))

# Join Method - List to String
langs = ["Python", "Java", "C"]
print(" - ".join(langs))

# Strip Method - Remove spaces
space_text = "   Python   "
print(space_text.strip())

# Checking Methods
print("Python".isalpha())    # Only letters?
print("123".isdigit())       # Only digits?
print("Python123".isalnum()) # Letters and digits?

