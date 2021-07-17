import random

player1=input("Enter Player1 name :::   ")
player2=input("Enter Player2 name :::   ")

toss_chose=random.randint(1,2)
if toss_chose==1:
    player=player1
else:
    player=player2

print(f"{player} Chose Your Toss")
toss=int(input("1.Head\n2.Tails\n"))



