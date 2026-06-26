'''
Encapsulation means hiding data and allowing controlled access to it through methods
and also uses access specifiers
'''
class Staff:
    def __init__(self):
        self.name = "Chay"  # Public(anyone can access and modify)
        self._gender='Male'# protected uses single' _ '(intended for internal use in class and its subclasses)
                           # (can be accessed and modified, only a naming convention)
        self.__salary=50000# private (Hidden from direct access outside the class.)
s1 = Staff()
print(s1.name)
print(s1._gender)
#print(s1.__salary) #Returns an error

#To access and modify private ones we use getter and setter methods
#those methods are not special,they are just methods
class Staff:
    def __init__(self):
           self.name = "Chay" 
           self._gender='Male'                 
           self.__salary=50000
    #Getter Method
    def view_salary(self):
          print('Salary:',end=" ")
          return self.__salary
    #Setter Method
    def modify_salary(self,salary):
          print('Salary Modified')
          self.__salary=salary
s1 = Staff()
print(s1.view_salary())#Calling Getter
s1.modify_salary(70000)#Calling Setter
print(s1.view_salary())

#By decorator:getters and setters can be implemented using decorators 
#(@property and @<property_name>.setter)
#A property allows you to access a method as if it were a variable (attribute).
#both getter and setter name should be same , and no need to use () while calling methods
class Staff:
    def __init__(self):
           self.name = "Chay" 
           self._gender='Male'                 
           self.__salary=50000
    #Getter Method
    @property
    def salary(self):
          print(self.name,'Salary:',sep="'s ",end=" ")
          return self.__salary
    #Setter Method
    @salary.setter
    def salary(self,salary):
          print('Salary Modified')
          self.__salary=salary
s1 = Staff()
print(s1.salary)#Calling Getter
s1.salary=70000#Calling Setter
print(s1.salary)#Calling Getter
