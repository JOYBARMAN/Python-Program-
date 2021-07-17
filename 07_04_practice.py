a=float(input("Enter number 1\n "))
b=float(input("Enter number 2\n "))
c=float(input("Enter number 3\n "))
d=float(input("Enter number 4\n "))

# if(a>b and a>c and a>d):
#     print("The greatest value is ",a)
# elif (b>a and b>c and b>d):
#     print("The greatest value is ",b)
# elif (c>a and c>b and c>d):
#     print("The greatest value is ",c)
# else:
#     print("The greatest value is ",d)


#another method

if(a>b):
    f1=a
else:
    f1=b
if(c>d):
    f2=c
else:
    f2=d

if(f1>f2):
    # f1=int(f1)
    print("The greatest number is ", f1)
else:
    # f2=int(f2)
    print("The greatest number is ", f2)

