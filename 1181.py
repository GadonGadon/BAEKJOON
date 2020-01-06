#1181_단어 정렬
#https://www.acmicpc.net/problem/1181
import sys;
def key_len(a):
    return len(a)
n = int(input())
a = []
for i in range(n):
    a.append(sys.stdin.readline().rstrip())
a.sort()
a.sort(key = key_len)
print(a[0])
p = a[0]
for i in range(1,n):
    if p != a[i]:
        print(a[i])
        p = a[i]



