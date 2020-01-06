#10870_피보나치 수 5
#https://www.acmicpc.net/problem/10870
def fibonachi(a):
    if a == 1:
        return 1
    if a == 0:
        return 0
    return fibonachi(a-1)+fibonachi(a-2)
n = int(input())
print(fibonachi(n))

