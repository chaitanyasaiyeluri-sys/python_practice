import random
print("Welcome To Rock Paper Scissors Game")
uip=input("enter your choice(rock,paper,scissors): ")#user input
rps=["rock","paper","scissors"]#list of options
rip=random.choice(rps)#random input 
if uip in rps:
    print(f"Computer choosed: {rip}\nYou choosed: {uip}")
    if uip==rip:
        print('It\'s a Draw')
    elif uip=="rock" and rip=="scissors":
        print("You Won")
    elif uip=="paper" and rip=="rock":
        print("You Won")
    elif uip=="scissors" and rip=="paper":
        print("You Won")
    else:
        print("Computer Won")
else:
    print('Input Error')
