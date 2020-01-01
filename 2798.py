n,m = map(int,input().split())

card = list(map(int, input().split()))
min = -1
#최대 100C3번
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            count = card[i] + card[j] + card[k] # 카드 3장의 합
            if count <= m and (m-count < m-min or min == -1): #합이 M보다 작고 가장 가까울경우
                min = count

print(min)
