# https://www.acmicpc.net/problem/1912
#

import sys
intput = sys.stdin.readline

N = int(input())
dp = [0]*N
# data = [int(input().split()) for _ in range(N)]
data = list(map(int,input().split()))
# print(data)

'''
구간의 합을 계속하다가 이전 위치의 구간의 합과 현재 위치의 값을 더했는데 이전의 값들의 구간의 합과 현재 위치의 값 중 max값을 선택.
dp[0] = data[0]
dp[1] = max(dp[0] + data[1], data[1])
dp[2] = max(dp[1] + data[2], data[2])
...
dp[n] = max(dp[n-1] + data(n), data[n])
예를 들어, [10, -4, 3, 1, 5, 6, -35, 12, 21, -1] 
현재 값이 -35이고, dp[5] = 21 이라고 하면,
dp[6] = max(dp[5] + data[6], data[6]) = max(21 - 35, -35) = -14
dp[7] = max(dp[6] + data[7], data[7]) = max(-14+12,12) = 12   <== 이전 합이 -2이고, 현재 값이 12라면 이전 구간합을 버린다.

'''

dp[0] = data[0]
for i in range(1,N):
    dp[i] = max(data[i], dp[i-1] + data[i])

# print(dp)        
print(max(dp))    

