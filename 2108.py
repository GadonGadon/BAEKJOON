#2108_통계학
#https://www.acmicpc.net/problem/2108
import sys
n = int(input())
a = [] #값을 입력받는 리스트
b = [0 for i in range(8001)] #최빈값을 구하기 위한 리스트
sum = 0
is_first = True

for i in range(n):
    temp = int(sys.stdin.readline().rstrip())
    sum += temp # 각 합을 계산
    a.append(temp)
    b[temp+4000]+=1

a.sort()
print("{:.0f}".format(float(sum/n))) #산술평균
print(a[n//2])#중앙값
max_count = max(b) #최빈값이 나온 횟수
count = 0
for i in range(8001):
    if b[i] == max_count: #이 값이 최빈값일경우 count+1
        count += 1
        m = i - 4000
    if count == 2:#count가 2일경우 --> 두번째로 작은 최빈값
        break

print(m) # 최빈값 출력
print(a[-1]-a[0]) # 범위 출력
