# A=[1,2,3,4]
# for i in range(len(A),0,-1):
#     print (i,end=" ")

A=[1,2,4,5]
# for i in range(A[-1],A[0],-1):
#     print (i,end=" ")
print(*reversed(A))
