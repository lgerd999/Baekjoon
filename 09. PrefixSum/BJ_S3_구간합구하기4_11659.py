#  https://www.acmicpc.net/problem/11659
# 누적합 기법을 이용하여 해결하는 문제

import sys

input = sys.stdin.readline

N,M = map(int,input().split())
data = list(map(int,input().split()))

prefix_sum = []

hap = 0
prefix_sum.append(0)
for i in data:
    hap += i
    prefix_sum.append(hap)

# print(prefix_sum)

for j in range(M):
    x,y = map(int,input().split())
    ans = prefix_sum[y] - prefix_sum[x-1]
    print(ans)
        

