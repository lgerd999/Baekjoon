# https://www.acmicpc.net/problem/2468
import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j,level):
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]
    
    visited[i][j] = 1
    Q = deque()
    Q.append([i,j])
    
    while Q:
        r,c = Q.popleft()
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]

            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue

            if data[nr][nc] > level and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                Q.append([nr,nc])                    

N = int(input())
a = 0
data = []
for _ in range(N):
    area = list(map(int,input().split()))    
    b = max(area)
    if a < b:
        a = b
    data.append(area)
#print(data,a)    
ans = 0
for l in range(a):
    count = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j] > l and visited[i][j] == 0:
                bfs(i,j,l)
                count += 1
    #print(count)            
    ans = max(ans,count)
print(ans)    