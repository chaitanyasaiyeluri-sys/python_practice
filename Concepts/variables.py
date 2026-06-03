"""
A variable is data container with a name 
it should start with a alphabet or underscore
it can only contain alphanumeric and underscore character
"""
#type() function is used to know the type of a varible or a value
"""
A comment is a line of additional info useful for the human reader
A comment is ignored by python during runtime
A single line comment begins with #
For multi line comments ,the line will be enclosed btw """ """
"""
#variables declaration
#basic
name='Chay'

#multiple
a,b,c=1,2,3
(x,y,z)=(10,20,30)
age,dob,height=19,"22/02/2007",5.4

print(f"Name= {name}\nAge= {age},Height= {height}\nDate Of Birth= {dob}")
print(f"a,b,c={a},{b},{c}")
print('x','y','z='+str(a),b,c,sep="-")
print('Type of a=',type(a),'\n''Type of DOB=',type(dob))
print(type(dob))