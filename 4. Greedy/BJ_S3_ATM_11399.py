# https://www.acmicpc.net/problem/11399

N = int(input())
data = list(map(int,input().split()))
data.sort()
ssum = 0
result = []
for i in data:
    ssum += i
    result.append(ssum)
print(sum(result))