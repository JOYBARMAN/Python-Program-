file=open('file.txt',"rb")
data=file.readline() # raed the first line from the text file
print(data)
data=file.readline() # raed the second line from the text file
print(data)
file.close()