f=open('poem.txt')
poem=f.read()

if "twinkle" in poem:
    print("Twinkle is present the poem")
else:
    print("Twinkle is not present")

f.close()