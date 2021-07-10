# https://www.acmicpc.net/problem/1003

DP = [[0]*2 for _ in range(41)]
DP[0][0] = 1
DP[1][1] = 1
for i in range(2,41):
    DP[i][0] = DP[i-2][0] + DP[i-1][0]
    DP[i][1] = DP[i-2][1] + DP[i-1][1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(DP[N][0],DP[N][1])