#Traditional Small House ,Big House Game
import random
num=int(input("Choose a Number between 0 to 12: "))
ran=random.randint(0,12)
if num in range(7):
    if ran<=6:
        print("Small House Won with",ran)
        if num==ran:
            print("You won 3x")
        else:
            print("You won 2x")
    else:
        print("you lost with",ran)
elif num in range(8,13):
    if 7<ran<=12:
        print("Big House Won with",ran)
        if num==ran:
            print("You won 3x")
        else:
            print("You won 2x")
    else:
        print("you lost with",ran)            
elif num==7:
    if ran==7:    
        print("Kingdom won \n","You won 3x")
    else:
        print("you lost with",ran)
else:
    print("Sorry for the inconvinience,Input Error Ocuured")




