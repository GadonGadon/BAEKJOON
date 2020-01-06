#11650_좌표 정렬하기
#https://www.acmicpc.net/problem/11650
import sys
def key2(a):
    return a[1]
n = int(input())
f = []
for i in range(n):
    x,y = (list(map(int,sys.stdin.readline().rstrip().split())))
    f.append((x,y))
f.sort(key = key2)
f.sort()
for i in range(n):
    print("%d %d\n"%(f[i][0],f[i][1]), end='')
