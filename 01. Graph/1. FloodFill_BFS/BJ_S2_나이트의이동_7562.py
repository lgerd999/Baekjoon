from collections import deque

def bfs(cord,I):
    rr = [-2,-2,-1,-1,1,1,2,2]
    cc = [-1,1,-2,2,-2,2,-1,1]
    visited = [[0] * I for _ in range(I)]
    queue = deque()
    queue.append(cord[0])
    visited[cord[0][0]][cord[0][1]] = 1
    while queue:
        r,c = queue.popleft()
        if r == cord[1][0] and c == cord[1][1]:            
            return visited[r][c]-1
        for i in range(8):
            nr = r + rr[i]
            nc = c + cc[i]
            if 0 <= nr < I and 0 <= nc < I and visited[nr][nc] == 0 :
                visited[nr][nc] = visited[r][c] + 1
                queue.append([nr,nc])    

N = int(input())
cord =[]
for _ in range(N):
    I = int(input())
    data = [list(map(int,input().split())) for _ in range(2)]
    cord.append([I, data])

for i,j in cord:        
    print(bfs(j,i))

# I = 8
# cord =[[0,0],[7,0]]