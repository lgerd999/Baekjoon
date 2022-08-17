
# https://www.acmicpc.net/problem/10819
# 3 <= N <= 8 범위를 가지므로 경우의 수는 6!로 완전 탐색의 풀이 가능
from itertools import permutations

N = int(input())
data = list(map(int,input().split()))

ans = 0
max_v = 0
for i in permutations(data):
    ans = 0
    for j in range(1,len(i)):
        ans += abs(i[j-1]-i[j])
    max_v = max(max_v,ans)        
print(max_v)    