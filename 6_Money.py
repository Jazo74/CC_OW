Money = 0
TenK = 0
FiveK = 0
TwoK = 0
OneK = 0
Hany = 0
Mar = 0
Money = int(input("Mennyi az osszeg?: "))
Hany = Money // 10
if Hany > 0:
    TenK = Hany
    Money = Money - 10 * Hany
Hany = Money // 5
if Hany > 0:
    FiveK = Hany
    Money = Money - 5 * Hany
Hany = Money // 2
if Hany > 0:
    TwoK = Hany
    Money = Money - 2 * Hany
OneK = Money // 1
print(TenK)
print(FiveK)
print(TwoK)
print(OneK)