#1011_Fly me to the Alpha Centauri
#https://www.acmicpc.net/problem/1011
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    n = y-x
    k = 0 #이전에 이동한 거리
    s = 1 #1부터 k+1까지의 합
    cnt = 0
    while n:
        if n >= s:
            k += 1
            s += (k+1)
            n -= k
            cnt += 1
        elif n >= s-k-1:
            n -= k
            cnt += 1
        else:
            s -= (k+1)
            k -= 1
            n -= k
            cnt += 1

    print(cnt)


