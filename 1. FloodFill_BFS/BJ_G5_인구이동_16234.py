# https://www.acmicpc.net/problem/16234

from collections import deque
def bfs(i,j):
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]
    
    pos = []
    visited[i][j] = 1
    Q = deque()  
    Q.append([i,j])  
    people = data[i][j]
    pos.append([i,j])
    cnt = 1
    while Q:        
        r,c = Q.popleft()        
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]

            if nr < 0 or nc < 0 or nr >= N or nc >= N :
                continue            
            
            if L <= abs(data[r][c] - data[nr][nc]) <= R and visited[nr][nc] == 0:
                #print(L,R,data[r][c],data[nr][nc])                
                people += data[nr][nc]
                pos.append([nr,nc])
                cnt += 1
                Q.append([nr,nc])
                visited[nr][nc] = 1    

    #print(visited,people,cnt)     
    for x,y in pos:
        data[x][y] = people//cnt
      
    return pos

N, L, R = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

ssum = 0
while True:    
    visited = [[0] * N for _ in range(N)]    
    isTrue = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                loc = bfs(i,j)
                if len(loc) > 1:
                    isTrue = True                                       
    if not isTrue:
        break
    ssum += 1                
print(ssum)            