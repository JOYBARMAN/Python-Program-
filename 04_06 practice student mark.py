mark1 = int(input("Enter student mark1 : "))
mark2 = int(input("Enter student mark2: "))
mark3 = int(input("Enter student mark3: "))
mark4 = int(input("Enter student mark4: "))
mark5 = int(input("Enter student mark5: "))
mark6 = int(input("Enter student mark6: "))
mark_list=[mark1,mark2,mark3,mark4,mark5,mark6]
mark_list.sort()
print(mark_list)
print("sum of mark list is",sum(mark_list))