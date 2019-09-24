count = 0
for i in range(999,100,-1):
    if count == 25:
        break
    if i % 7 == 0 or i % 9 == 0:
        print(str(count+1) + ". " +str(i))
        count += 1