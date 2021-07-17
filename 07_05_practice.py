sub1=int(input("Enter subject 1 marks :  "))
sub2=int(input("Enter subject 2 marks :  "))
sub3=int(input("Enter subject 3 marks :  "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail in the exam")

elif (sub1+sub2+sub3)/3<40:
    print("you are fail in the exam due to low marks ")
else: 
    print("congrats !!!! you are pass the exam ")

    
