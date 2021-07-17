num=int(input("Enter your number  ::::  "))
prime=True
for i in range(2,num):
    if (num%i==0):
        prime=False
        break
    else:
        prime=True

if prime:
    print("The num is Prime")
else:
    print("The num is not Prime")

