# creating an empty list
mylist = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	element = int(input())

	mylist.append(element) 
	
print(mylist)

def merge_sort(mylist):
    
    lefthalf=mylist[:4]
    righthalf=mylist[4:]

    print(lefthalf,righthalf)

    lefthalf_lefthalf=lefthalf[:2]
    lefthalf_righthalf=lefthalf[2:]
    righthalf_lefthalf=righthalf[:2]
    righthalf_righthalf=righthalf[2:]

    print (lefthalf_lefthalf,lefthalf_righthalf,righthalf_lefthalf,righthalf_righthalf)

    print(lefthalf_lefthalf[:1],lefthalf_lefthalf[1:],lefthalf_righthalf[:1],lefthalf_righthalf[1:],righthalf_lefthalf[:1],righthalf_lefthalf[1:],righthalf_righthalf[:1],righthalf_righthalf[1:])

    value1=sorted(lefthalf_lefthalf)
    value2=sorted(lefthalf_righthalf)
    value3=sorted(righthalf_lefthalf)
    value4=sorted(righthalf_righthalf)

    print([value1[0]],[value1[1]],[value2[0]],[value2[1]],[value3[0]],[value3[1]],[value4[0]],[value4[1]])

    lefthalf=[value1[0],value1[1],value2[0],value2[1]]
    righthalf=[value3[0],value3[1],value4[0],value4[1]]

    print(sorted(lefthalf),sorted(righthalf))

    sorted_list=sorted(lefthalf)+sorted(righthalf)
    print(sorted(sorted_list))


print(merge_sort(mylist))