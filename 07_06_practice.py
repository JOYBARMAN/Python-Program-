commennt=input("Enter your comment\n")

# if(commennt=="make a lot of money" or commennt=="buy now" or commennt=="subscribe this" or commennt=="click this"):
#     print("This is a spam message")
# else:
#     print("None")


# another way

if("make a lot of money" in commennt):
    spam=True
elif("subscribe this" in commennt):
    spam=True
elif("buy now" in commennt):
    spam=True
elif("click this" in commennt):
    spam=True
else:
    spam=False


if(spam==True):
    print("This is a spam message dont belive")
else:
    print("This is not spam you can continue")