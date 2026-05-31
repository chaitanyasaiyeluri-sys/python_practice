#conditional statements executes code if condition is true
'''
if statement:
executes a block of code if the condition is true
#pass keyword is used to avoid empty conditional statements to avoid execution error ,it makes the code pass
Syntax: 
if condition :
    statements

after the condition : is compulsory,which defines the if block
after the if statement indendation should be correctly given as a tab or 4 spaces
'''
if True:
    print("if statement")

"""
if else statement:
in the case of failure of if condition else statements are executed
"""
if 10>11:
    print('10 is bigger than 11' )
else:
    print('11 is bigger than 10',"printed from else")

'''
if elif else statements
checks multiple statements executes only one true one ,the remaining statements are terminated on reaching the true one
we can use multiple elif statements but only one if and one else statement in standard form
'''
print('Printed using if elif else statements:')
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#Nested if else
age=15
if age>=18:
    print('eligible to vote')
    if age<18:
        print('ineligible for voting')
    else:
        print("under age")
else:
    print("try after 18 years")

# Short-hand if
age = 20

if age >= 18: print("Adult")


# Short-hand if-else (Ternary Operator)
age = 20

print("Adult") if age >= 18 else print("Minor")

if True:
    pass