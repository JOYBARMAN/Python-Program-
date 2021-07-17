num=int(input("Enter you number for multipication table ::::   "))


def multipication(num):
    for i in range(1,11):
        print (f"{num}  *  {i} = {num*i}")
        

print(multipication(num))