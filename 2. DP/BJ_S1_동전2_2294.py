# https://www.acmicpc.net/problem/2294
import sys
input = sys.stdin.readline
INF = sys.maxsize

N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins.sort()    # 가장 작은 coin부터.

DP = [INF]*(K+1)
DP[0] = 0
for i in range(coins[0],K+1): # 첫 동전(가장 작은 값)위치부터 값이 1이므로 coins[0] 부터 시작
    for j in coins:
        if i-j >= 0:    # 해당 조건문 삭제시 index error 발생
            '''
            동전 개수만큼 반복하면서 DP[i - 동전[j]] + 1 값 중 최소 값을 DP[i]에 저장
            K=0 ~ 15
             [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 1, 2, 3, 3]
            '''
            DP[i] = min(DP[i],DP[i-j]+1)   
#print(DP)
print(DP[K] if DP[K] != INF else -1)