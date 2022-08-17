# https://www.acmicpc.net/problem/2156
# 계단오르기(https://www.acmicpc.net/problem/2579) 문제와 유사

import sys
input = sys.stdin.readline

N = int(input())
# dp[0] ~ dp[2]까지 변수 선언을 위해 N +2 개 정도 미리 선언해 준다.
data = [0] * (N+3)
dp= [0] * (N+3)
#  선언해 주었으면, 대입식으로 해주어야 index 에러가 안난다. 아래와 같이 입력하면 에러 발생.
#  data = [int(input()) for _ in range(N)]
for i in range(N):
    data[i] = int(input())

dp[0] = data[0]
dp[1] = data[0] + data[1]
dp[2] = max(dp[0]+data[2],data[1]+data[2],dp[1])
for i in range(3,N):    
    # 현재 위치에서 이전 마신 양을 근거로 계산해야 함. 계단 오르기 문제와 유사.
    # 1. 현재 위치 i를 마시고, dp[i-2]까지 마신 양 
    # 2. i , i-1 번재 포도주를 마시고 dp[i-3]까지 마신 양
    # 3. 현재 위치 i를 마시지 않고 dp[i-1]까지 마신 양
    # 1~3중 최대가 되는 값이 현재 최대 포도주 마신 양이 됨.
    dp[i] = max(dp[i-2] + data[i], dp[i-3]+data[i-1]+data[i],dp[i-1])

# print(dp)        
print(dp[N-1])