#4948_베르트랑공준
#https://www.acmicpc.net/problem/4948
prime_number = [2]
for i in range(3, 123456*2+1, 2):
    is_prime = True
    for j in prime_number:
        if i % j == 0:
            is_prime = False
            break
        if j**2 > i: #에라토스테네스의 체
            break

    if is_prime:
        prime_number.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in prime_number:
        if i > n*2:
            break
        if n < i and i <= n*2:
            count += 1
    print(count)