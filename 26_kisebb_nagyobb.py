N = 0
M = 0
Min = 50000
Max = -50000
N = int(input("Hány számot adsz meg? :"))
for i in range(N):
    M = int(input("Adj meg egy számot: "))
    if M < Min:
        Min = M
        print("Ez a szam eddig a legkisebb. (" + str(Min) + ")")
    else:
        print("Van mar ettol kisebb szam is. (" + str(Min) + ")")
    if M > Max:
        Max = M
        print("Ez a szam eddig a legnagyobb. (" + str(Max) + ")")
    else:
        print("Van mar ettol nagyobb szam is. (" + str(Max) + ")")
    print()
