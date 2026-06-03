#lenght of a list,list is the para
def lenght(list):
    print("Lenght of list is:",len(list))
lenght([1,2,3,4,5,6,7,8,9,10])

#print elements of a list in a single line ,list is the para
def ele(list):
    for i in list:
        print(i,end=" ")
ele(['a','b','c','d','e','f'])

#factorial of n ,n is the para
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
n=int(input('\nEnter a num to get its factorial: '))
print('Factorial of',n,'is:',fact(n))

#even or odd function
def check(a):
    if a%2==0:
        print(a,'is Even Number')
    else:
        print(a,'is Odd Number')

check(int(input('Enter a number to check is it even or odd: ')))

#sum of first n natural nums using recursion
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
n=int(input('enter a number n to get sum of first n natural numbers : '))
print('sum=',sum(n))

#print elements of a list using list and index as parameters ny recursion
def ele(list,idx):#we can also initial idx=0 so that we dont have to pass the idx argument
    if idx==len(list):
        return
    print(list[idx])
    idx +=1
    ele(list,idx)

print("Printing list elements using Recursion:")
ele(['a','b','c','d','e','f'],0)
