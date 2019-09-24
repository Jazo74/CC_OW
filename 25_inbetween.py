szoveg = ""
be = False
sor = False
szoveg = input("Kerem a szoveget: ")
for i in range(len(szoveg)):
    if ord(szoveg[i:i+1]) == ord("<"):
        be = True
    elif ord(szoveg[i:i+1]) == ord(">"):
        be = False
        sor = True
    if be == True and ord(szoveg[i+1:i+2]) != ord(">"):
        print(szoveg[i+1:i+2],end="")
    if sor == True:
        print()
        sor = False
