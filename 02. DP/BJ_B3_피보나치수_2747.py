# https://www.acmicpc.net/problem/2747
# 피보나치 수
N = int(input())

dp = [0]*100
dp[0],dp[1] = 1,1
for i in range(2,N):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[N-1])
