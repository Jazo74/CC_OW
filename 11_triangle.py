a = 0
koz = ""
csillag = "*"
a = int(input("szam: "))
koz = " " * a
for i in range(0,a):
    print(koz + csillag + koz)
    csillag += "**"