mydic={
    "tabil":"table",
    "cha" : "tea",
    "boi": "book",
    "pakha":"fan",
    "kolom":"pen",

}
a=input("enter any bangla word :  ")
# print("the meaning of bangla word is- ",mydic[a])

print("the meaning of bangla word is- ",mydic.get(a))    # this line will not give any error