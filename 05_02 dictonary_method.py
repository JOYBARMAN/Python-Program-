dic ={
    "li" : ["joy",34,66,6854,466],
    "joy":"a software engineer",
    "bangladesh":"is a beautiful country",
    "harry":"one of the best python techer",
    1:2,
    "nested_dic":{
        "apple":"kind of fruit",
        "rose":"kind of flower",
        }

}
dic[1]=6
dic["joy"]="a begineer software engineer"

print(dic.keys()) #print the dictionary key
print(dic.values()) #print the dictionary values
# print(dic.items())
update_dic={
    "rohan":"friend",
    "diya":"friend"
}
dic.update(update_dic) #for update the dictionary
dic.update({"leon":"friend"})
print(dic.items())     #print the key value of all content to the dictionary
print(dic.get("joy"))  #print the value associated the key "joy" 