#7568 덩치
#https://www.acmicpc.net/problem/7568
n = int(input())
p = []
for i in range(n): #최대 50
    a = list(map(int,input().split()))
    a.append(0)
    p.append(a)

for i in range(n):
    count = 1
    for j in range(n):
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            count += 1
    p[i][2] = count

for i in range(n):
    print(p[i][2], end = ' ')
print()