a = 0
b = 0
c = 0
control = False
a = int(input("Kérem az a-t: "))
b = int(input("Kérem az b-t: "))
c = int(input("Kérem az c-t: "))
control = a*a+b*b == c*c
if control == True:
    print("Ez derékszögű háromszog.")
elif a+b <= c:
    print("Ez nem is háromszog.")     
else: 
    print("Ez nem derékszögű háromszog.")