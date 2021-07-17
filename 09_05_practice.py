def celcious_to_farenhite(cel):
    farenhite=(1.8*cel)+32
    return farenhite
def farenhite_to_cecious(faren):
    celcious=(5*faren-160)/9
    return celcious

press=int(input(''' \n1.Enter one to convert celcious to farenhite\n2.Enter two to convert farenhite to celcious\nPress 1 or 2\n'''))

if press==1:
    cel=float(input("Enter Celcious scale temperature ::   "))
    print(f"Your {cel} celcious temoarature in farenhite is ",celcious_to_farenhite(cel))
else:
    faren=float(input("Enter Farenhite scale temperature ::   "))
    print(f"Your {faren} farenhite temparature in celcious is ",farenhite_to_cecious(faren))
