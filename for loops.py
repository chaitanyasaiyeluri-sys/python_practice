'''
for loop is used to iterate over a sequence
Syntax:
for variable in sequence:
    # code

range funtion:
range(start,stop,step)
stop is excluded
step is 1 defaultly
'''
for i in range(6):
    print(i)
    if i == 3:
        print('stop at 3')
        break
        
else:
    print('else')


#factorial of n using for loop
print('Fact=',tot)
n=int(input('Enter a number to get Factorial of  that number: '))
fact=1
for i in range(1,n+1):
    fact *=i
print('factorial of',n,'is :',fact)