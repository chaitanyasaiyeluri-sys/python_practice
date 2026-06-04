'''
A file saves your data permanently on your storage 
# open("file", "r") -> Read file
# open("file", "w") -> Write (overwrite)
# open("file", "a") -> Append

# read()      -> Read entire file
# readline()  -> Read one line
# readlines() -> Read all lines as list
# write()     -> Write data
# close()     -> Close file

# tell()      -> Current cursor position
# seek(0)     -> Move cursor

# with open() -> Recommended way (auto close)
'''
# f=open('C:/Users/sai/Git/python_practice/Concepts/Tuples.py')
# data=f.read()
# print(data)
# f.close()

# File Handling in Python

# "w" mode -> Create file if it doesn't exist
# If file exists, old content is deleted and replaced
with open("data.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to File Handling")

# "r" mode -> Read file contents
with open("data.txt", "r") as file:
    print("\n--- read() : Read Entire File ---")
    print(file.read())

# readline() -> Read one line at a time
with open("data.txt", "r") as file:
    print("\n--- readline() : Read First Line ---")
    print(file.readline())

# readlines() -> Read all lines into a list
with open("data.txt", "r") as file:
    print("\n--- readlines() : Read All Lines as List ---")
    print(file.readlines())

# "a" mode -> Append data to end of file
with open("data.txt", "a") as file:
    file.write("\nThis line was appended")

# Read file after appending
with open("data.txt", "r") as file:
    print("\n--- File After Append ---")
    print(file.read())

# Loop through file line by line
with open("data.txt", "r") as file:
    print("\n--- Loop Through File ---")
    for line in file:
        print(line.strip())  # strip() removes extra newline

# File Properties
with open("data.txt", "r") as file:
    print("\n--- File Properties ---")
    print("File Name :", file.name)
    print("Mode      :", file.mode)
    print("Closed    :", file.closed)#file is still opened.
    #file closed only after the ending of with open block

# tell() -> Current cursor position
with open("data.txt", "r") as file:
    print("\n--- tell() ---")
    print(file.tell())

    # seek(0) -> Move cursor to beginning
    file.seek(0)

    print("\n--- After seek(0) ---")
    print(file.read())

# close() example (manual method)
file = open("data.txt", "r")
print("\n--- Manual Close ---")
print(file.read())
file.close()

print("File Closed :", file.closed)
