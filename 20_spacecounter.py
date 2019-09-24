Mondat = ""
Counter = 0
Space = " "
Mondat = input("Kerem a mondatot: ")
for i in range(len(Mondat)):
    if ord(Mondat[i:i+1]) == ord(Space):
        Counter += 1
print(Counter)