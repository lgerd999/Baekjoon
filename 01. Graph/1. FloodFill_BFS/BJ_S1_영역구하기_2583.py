
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N,M,K = map(int,input().split())    # N : column, M : row
graph = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def rect(s1,e1,s2,e2):    
    for i in range(e1,e2):
        for j in range(s1,s2):            
            graph[i][j] = 1
    # print(graph)        

def bfs(i,j):
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]    
    
    Q = deque()
    Q.append([i,j])
    cnt = 1
    visited[i][j] = 1
    while Q:
        r,c = Q.popleft()
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]
            
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            
            if graph[nr][nc] == 0 and visited[nr][nc] == 0:
                cnt += 1
                visited[nr][nc] = 1                
                Q.append([nr,nc])        
    return cnt    
    
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    rect(x1,y1,x2,y2)

ans = []
area = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and visited[i][j] == 0:
            ans.append(bfs(i,j))
            area += 1
    
print(area)    
print(*sorted(ans))
