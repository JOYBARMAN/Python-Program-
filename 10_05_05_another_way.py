def game():
    return 80

score=game()

f=open('highscore.txt')
highscore=int(f.read())
f.close

if highscore<score:
    f=open('highscore.txt','w')
    f.write(str(score))
    f.close
else:
    print("highscore is = ",highscore)