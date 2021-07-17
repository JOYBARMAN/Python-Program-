#sum of first natural num
def sum_of_range(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print (sum)
    
n=int(input("Enter range ::  "))
print (sum_of_range(n))