# n=int(input("Enter number :: "))
# prime=False

# for i in range(2,n-1):
#     if (n%i==0):
#         prime=False
#         break
#     else:
#         prime=True


# if prime:
#     print("prime")
# else:
#     print('not prime')


# print all prime number from 1 to 100



for i in range(1,101):
    if i>1:
        for j in range(2,i):
            # for k in range(2,j):
            if (i%j==0):
                print(f"{i} not prime")
                break
            else:
                print(f"{i} prime")
                
    

