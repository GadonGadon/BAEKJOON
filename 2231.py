n = int(input())
check = True
for i in range(1,n): # 최대 1,000,000
    s = str(i)
    count = 0
    for j in s: # 최대 7
         count += int(j)
    count += i
    if count == n:
        print(i)
        check = False
        break

if check == True:
    print(0)