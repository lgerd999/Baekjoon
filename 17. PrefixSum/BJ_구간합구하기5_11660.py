# https://www.acmicpc.net/problem/11660
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