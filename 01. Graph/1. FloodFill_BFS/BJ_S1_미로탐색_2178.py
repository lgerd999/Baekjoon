# https://www.acmicpc.net/problem/2178
from collections import deque

def bfs(data,i,j):    
    visited = [[0] * M for _ in range(N)]
    queue_r = deque()
    queue_c = deque()
    
    rr = [1,-1,0,0]
    cc = [0,0,1,-1]
	
    queue_r.append(i)
    queue_c.append(j)
    visited[i][j] = 1

    while queue_r and queue_c:
        r = queue_r.popleft()
        c = queue_c.popleft()
        for i in range(4):
            nr = r + rr[i]
            nc = c + cc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= M :                
                continue            
            if data[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1 
                queue_r.append(nr)
                queue_c.append(nc)
    print(visited)
    return visited[N-1][M-1]	

# N, M = list(map(int,input().split()))
# data = [list(map(int, input())) for _ in range(N)]

# print(data)

N,M = 4,6
#data =[[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]] #15
data =[[1,1,0,1,1,0],[1,1,0,1,1,0],[1,1,1,1,1,1],[1,1,1,1,0,1]] #9

# N,M= 2,25
# data = [[1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1],
#         [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1]]
print(bfs(data,0,0))


			