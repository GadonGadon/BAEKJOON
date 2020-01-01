#9020_골드바흐의 추측
#https://www.acmicpc.net/problem/9020
prime_number = [2]
b = [0,0,1]
# 2 부터 10000까지의 소수를 전부 구해둔다.
for i in range(3, 10001, 2):
    is_prime = True
    for j in prime_number:
        if i % j == 0:
            is_prime = False
            break
        if j**2 > i: #에라토스테네스의 체
            break

    if is_prime:
        prime_number.append(i)
        b.append(1)
        b.append(0)
    else:
        b.append(0)
        b.append(0)

t = int(input())
for j in range(t):
    n = int(input())
    min = 100000
    a = []
    for i in prime_number:
        temp = n - i
        if temp < 0 or temp < i: #뒤의 숫자가 앞의 숫자보다 클경우 종료
            break
        if b[temp]:
            if temp - i < min: #두 소수의 차이가 가장 작을경우
                min = temp - i
                a = [i, temp]

    print(a[0], a[1])


