value1=int(input("Enter value one :: "))
value2=int(input("Enter value two :: "))
value3=int(input("Enter value three  :: "))
value4=int(input("Enter value four :: "))

my_list=[value1,value2,value3,value4]

large_value=my_list[0]

for i in my_list:
    if i>large_value:
        large_value=i
        print("The large value is ",large_value)