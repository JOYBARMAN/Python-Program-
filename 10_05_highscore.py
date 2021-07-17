def game():
    return 70

score=game()

with open("highscore.txt") as f:
    highscore=int(f.read())

if highscore<score:
    with open("highscore.txt","w") as f:
        f.write(str(score))
else:
    print("highscore is = ",highscore)
