def calculator():
    def mysum(num1,num2):
        sum=num1+num2
        return sum
    def mysub(num1,num2):
        sub=num1-num2
        return sub
    def mymul(num1,num2):
        mul=num1*num2
        return mul
    def mydiv(num1,num2):
        div=num1/num2
        return div

    num1=int(input("Enter number one :::  "))
    num2=int(input("Enter number two :::  "))


    press=int(input('''\n\n1.Summstion\n2.Subtraction\n3.Multipication\n4.Subtraction\nEnter Any.... '''))

    if press==1:
        print(mysum(num1,num2))
    elif press==2:
        print(mysub(num1,num2))
    elif press==3:
        print(mymul(num1,num2))
    else:
        print(mydiv(num1,num2))
calculator()



    
    