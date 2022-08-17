# https://www.acmicpc.net/problem/11660
'''
# 포함배제원리를 이용한 2차원 누적합
S[i][j] = (1,1) ~ (i,j)의 합
S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + A[i][j]

(1,1)
 ---------------------
| S[i-1][j-1]   |    |
| (중첩되어 있어 |  ==|> S[i-1][j]
| 빼줘야함)     |    |
|---------------|----|
| S[i][j-1]     |  ==|> A[i][j]
 --------------------- (i,j)
 
예를 들어, 
 (1,1)              b     d
    ---------------------
    | S[a-1][b-1]   |    |
    | (두번 빠짐)    |  ==|> S[a-1][d]
    |               |    |
a   |---------------|----|(a-1,d)
    | S[c][b-1]     |  ==|> S[c][d]
c   --------------------- (c,d)
                  (c,b-1)
 S[c][d] - S[c][b-1] - S[a-1][d] + S[a-1][b-1] = A[c][d]
 
'''

import sys
input = sys.stdin.readline
result = []
N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
DP = [[0]* (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        DP[i][j] = DP[i][j-1] + data[i-1][j-1]        
for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    ans = 0
    for j in range(x1,x2+1):
        ans += DP[j][y2] - DP[j][y1-1]
    result.append(ans)
print(*result,sep='\n')