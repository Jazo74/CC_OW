x = 1
y = 0
z = 0
N = 0
Osszeg = 0
N = int(input("Szam?: "))
print()
for i in range(N):
    print(str(z) + " + ")
    Osszeg += z
    z = x + y
    x = y
    y = z
print("Osszeg =" + str(Osszeg))