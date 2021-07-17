mylist=[4,5,1,2]
value=mylist[0]

for i in mylist:
    if i>value:
        value=i
        # return value
        print("large",value)
