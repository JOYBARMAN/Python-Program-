import random

# Find who is win in the game

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False
    


print("computer_turn : Snake(s), Water(w) , Gun(g)")

#import random & convert random number into s,w or g

random=random.randint(1,3)
if random==1:
    comp='s'
elif random==2:
    comp='w'
else:
    comp='g'

try:
    you=input("your turn:  chose anyone Snake(s), Water(w) , Gun(g) \n")
except Exception as e:
        print (e)

print("-"*100)

print(f"Computer Chose:{comp}\nYou chose:{you}")
print("-"*100)

#Find gamewin function result & convert into win or lose

win=gamewin(comp,you)

if win==None:
    print ("Game Tie")
elif win==True:
    print("You win")
else:
    print("You Lose  !!!")

