'''A while loop executes a block of code repeatedly as long as the condition is True.
syntax:
while condition :
    code
'''
#printing 1 to 100 numbers
i=1
while i<=100:
    print(i,end=" ")
    i +=1

#printing 100 to 1
i=100
print()
while i>=1:
    print(i,end=" ")
    i -=1

#printing multiplication table of number n
n=int(input("Enter a number: "))
print(f'Multiplicatioin Table of {n}:')
i=1
while i<=10:
    print(n,"x",i,'=',n*i)
    i +=1

#print the elements of the list using loop [1,2,3,4,5,6,7,8,9,10]
i=0
list=[1,2,3,4,5,6,7,8,9,10]
while i<=(len(list)-1):
    print(list[i])
    i +=1

#search num X in a tuple using loop
tup=(9,93,7,5,46,6,2,0,1)
print('elements of tuple:',tup)
x=int(input('Enter an element for searching index: '))
i=0
while i<len(tup):
    if x==tup[i]:
        print(x,'Found at index',i)
    else:
        print('searching...')
    i +=1

#factorial of n using while loop    
i=1
n=int(input('Enter a number to get Factorial of  that number: '))
tot=1
while i <=n :
    tot *=i
    i +=1
