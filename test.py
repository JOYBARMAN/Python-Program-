# if __name__ == '__main__':
#     n = int(input("Enter Num :: "))
#     for i in range(0,n):
#         print(i*i)



def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
        

year = int(input())
print(is_leap(year))
