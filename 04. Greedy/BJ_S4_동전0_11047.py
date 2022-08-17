# https://www.acmicpc.net/problem/11047
N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
cnt = 0
for i in range(len(coins)):
    Q = K // coins[i]
    K -= Q*coins[i]
    cnt += Q
print(cnt)    