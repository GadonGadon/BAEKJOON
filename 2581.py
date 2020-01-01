# 2581_소수
#https://www.acmicpc.net/problem/2581
n = int(input())
m = int(input())
prime_number = [2]
count = 0
is_min = True
minimum = 0

for i in range(3, m+1, 2):
    is_prime = True
    for j in prime_number:
        if i % j == 0:
            is_prime = False
            break
        if j**2 > i: #에라토스테네스의 체
            break

    if is_prime:
        prime_number.append(i)

for i in prime_number:
    if i > m:
        break
    if i >= n:
        count += i
        if is_min:
            minimum = i
            is_min = False
if not is_min:
    print(count)
    print(minimum)
else:
    print(-1)