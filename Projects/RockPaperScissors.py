import random
print("Welcome To Rock Paper Scissors Game")
uip=input("enter your choice(rock,paper,scissors): ")
rps=["rock","paper","scissors"]
rip=random.choice(rps)
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
