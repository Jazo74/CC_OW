a = 0
a1 = 0
b = 0
b1 = 0
c = 0
c1 = 0
Max = 0
control = False
a = int(input("Kérem az a-t: "))
b = int(input("Kérem az b-t: "))
c = int(input("Kérem az c-t: "))
if a >= b:
    if a >= c:
        c1 = a
        b1 = b
        c1 = c
    elif c >= a:
        c1 = c
        a1 = a
        b1 = b
elif b >= a:
    if b >= c:
        c1 = b
        a1 = a
        b1 = b
    elif c >= b:
        c1 = c
        a1 = a
        b1 = b
    
control = a1*a1+b1*b1 == c1*c1
if control == True:
    print("Ez derékszögű háromszog.")
elif a1+b1 <= c1:
    print("Ez nem is háromszog.")     
else: 
    print("Ez nem derékszögű háromszog.")