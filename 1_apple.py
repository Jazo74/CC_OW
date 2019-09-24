AppleUnitPrice = 12
AppleWeight = 3
ApplePrice = 0
ApplePrice = AppleUnitPrice * AppleWeight
print(ApplePrice)
AppleUnitPrice = int (input("Add meg az alma egysegarat:"))
AppleWeight = int (input("Add meg az alma sulyat:"))
ApplePrice = AppleUnitPrice * AppleWeight
print("Az vasarolt alma ara " + str(ApplePrice) + " korona.")