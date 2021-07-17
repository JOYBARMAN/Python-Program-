letter=''' Dear NAME,
Congratulation, you are selected as a software engineer in AVS company. 
Thanks & Regards joy
Date : DATE '''
name=input("Enter Your Name : \n")
date=input("Enter Today date : \n")
letter=letter.replace("NAME",name)
letter=letter.replace("DATE",date)
print(letter)