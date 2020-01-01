#3009_네 번째 점
#https://www.acmicpc.net/problem/3009
x= []
y= []
for i in range(3):
    a,b = list(map(int,input().split()))
    x.append(a)
    y.append(b)

for j in range(3):
    for k in range(j+1,3):
        if len(x) == 3 and x[j]==x[k]:
            x[j] = 1001
            x[k] = 1001
            break
for j in range(3):
    for k in range(j+1,3):
        if len(y) == 3 and y[j] == y[k]:
            y[j] = 1001
            y[k] = 1001
            break

for i in range(3):
    if x[i] != 1001:
        print(x[i], end = ' ')
for i in range(3):
    if y[i] != 1001:
        print(y[i], end = ' ')
