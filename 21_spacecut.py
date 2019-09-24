Mondat = ""
Mondat2 = ""
Mondat3 = ""
Space = " "
Mondat = input("Kerem a mondatot: ")
print()
Mondat2 = Mondat.replace(" ","")
print(Mondat2)
print()
for i in range(len(Mondat)):
    if ord(Mondat[i:i+1]) != ord(Space):
        Mondat3 += Mondat[i:i+1]
print(Mondat3)