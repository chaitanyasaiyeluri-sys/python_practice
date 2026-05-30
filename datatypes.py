#data type describes which type of data a variable stores

#numeric types are 3 :int,float,complex
#they dont need quotes like srings while assining or printing
print("22 is",type(22))
print("2.2 is",type(2.2))
print("2+2j is",type(2+2j))

#text type: string ,they should always enclosed by quotes
#strings can be enclosed by " " or ' ' or ''' ''' or """ """
print("chay is ",type("chay"))
print("""hi""")

#boolean type: bool:True,False 
#their first letter should be capitalized
print("True is",type(True))

#None type :None the first letter is capital,used when there is no value to a variable
print("None is",type(None))


a=range(6)
print(*a)