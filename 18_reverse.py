str1 = ""
betu = 0
str1 = input("Mondat?: ")
betu = len(str1) - 1
for i in range(len(str1)):
    print(str1[betu:betu+1],end="")
    betu -= 1
print()