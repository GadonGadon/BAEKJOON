#10989_수 정렬하기 3
#https://www.acmicpc.net/problem/10989
import sys
n = int(input())
a = [0 for i in range(10001)]
for i in range(n):
    a[int(sys.stdin.readline().rstrip())] += 1
for i in range(10001):
    if a[i]:
        print('%s\n'%i*a[i], end = '')
