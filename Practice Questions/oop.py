class student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def average(self):
        print('Average marks for',self.name,'is:',(self.m1+self.m2+self.m3)/3)

s1=student('chay',90,80,70)
s1.average()
