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
#for loop with range
for i in range(6):
    print(i)
    if i == 3:
        print('stop at 3')
        break
        
else:
    print('else')

#for loop with variable
nums=[1,2,3,4,5,6,7,8,9,10]
for i in nums:
    print(i,end=" ")
#factorial of n using for loop
n=int(input('Enter a number to get Factorial of  that number: '))
fact=1
for i in range(1,n+1):
    fact *=i
print('factorial of',n,'is :',fact)
