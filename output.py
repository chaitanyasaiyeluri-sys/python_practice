"""
we use print() to display the output
"""
#method 1
print("1.Hello, World! using print()") #basic OP

#method 2: printing a variable
a="2.Hello, World!"
print(a)

#method 3: printing multi values,text using coma, coma adds a single space automatically
a="Hello, World!"
print("3.Text:",a,"From","Python")

#method 4: plus(+) is used to join/concate Strings
b=22
print("4.Text: "+a + ' '+str(b)+' using +')

#method 5: f-Strings,modern way to join text and variables
#syntax: printf(f"text {variable}")
print(f"5.Hello, World! {b} using f-String")

#method 6: .format inserts any values/variables into placeholders
print("6. B= {},Nums= {}".format(b,'1 2 3 4'))

#method 7: sep="" replaces the default space with custom type
print("7.1",2,3,4,sep=',')

#method 8: end"=" prints the upcomming line in the same line with a custom ending
print(f"8.Loading",end='.... ')
print('code')

#method 9: \n printing in new lines while in same print statement, \n is used only inside ""
print("9.First\n"," Second","\n"," Third")

