m = 0
n = 0
StrA = ""
m = int(input("m?: "))
n = int(input("n?: "))
for i in range(1,n+1):
    if i == 1 or i == n:
        StrA = "*" * m
    else:
        StrA = ("*" + (int(m-2) * " ") + "*")
    print(StrA)