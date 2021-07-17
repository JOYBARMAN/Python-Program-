file=open("file.txt","r")
# data=file.read()
data=file.read(7)  #read 7 character in the file 
print(data)
file.close()