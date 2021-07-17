def sum(a,b):
    sum=a+b
    return (sum)
def sub(a,b):
    sub=a-b
    return (sub)
def mul(a,b):
    mul=a*b
    return (mul)
def div(a,b):
    div=a/b
    return (div)
num1=int(input("num 1 : "))
num2=int(input("num 2 : "))
c=sum(num1,num2)
d=sub(num1,num2)
e=div(num1,num2)
f=mul(num1,num2)
print("1.enter 1 for sum\n2.enter 2 for sub\n3.enter 3 for mul\n4.enter 4 for div")
p=int(input("enter anyone\n"))
if (p==1):
    print("the summation is = ",c)
elif (p==2):
    print("the subtraction is is = ",d)
elif (p==3):
    print("the multipication is = ",f)
elif (p==4):
    print("the divition is = ",e)
    
    


