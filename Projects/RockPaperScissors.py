import random
print("Welcome To Rock Paper Scissors Game")

rps=["rock","paper","scissors"]#list of options
play="yes"
u_score=0
c_score=0

def check(u_score,c_score):
    rip=random.choice(rps)#random input 
    uip=input("enter your choice(rock,paper,scissors): ").lower()#user input
    if uip in rps:
        print(f"Computer choosed: {rip}\nYou choosed: {uip}")
        if uip==rip:
            print('It\'s a Draw')
        elif uip=="rock" and rip=="scissors":
            print("You Won")
            u_score +=1
        elif uip=="paper" and rip=="rock":
            print("You Won")
            u_score +=1
        elif uip=="scissors" and rip=="paper":
            print("You Won")
            u_score +=1
        else:
            print("Computer Won")
            c_score +=1
        print(f"Score:\nYou: {u_score}\t\tComputer: {c_score}")
        return u_score,c_score
    else:
        print('Input Error')

while play=="yes":
    u_score,c_score=check(u_score,c_score)
    play="no"
    print()
    play=input('Do you play again (yes/no):').lower()
else:
    u_score=0
    c_score=0
    print("Game over!")
    quit()
     