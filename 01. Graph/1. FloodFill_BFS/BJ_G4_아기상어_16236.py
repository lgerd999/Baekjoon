# https://www.acmicpc.net/problem/16236
# 참조 : https://chldkato.tistory.com/54
from collections import deque
import sys
def matrix_print(grid):
    for i in range(len(grid)):
        for j in grid[i]:
            print(j,end=' ')
        print()    

def bfs(r,c,size,time,fish):
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]

    visited = [[-1] * N for _ in range(N)]   
    visited[r][c] = time
    pos = []
    Q = deque()
    Q.append([r,c])
    
    while Q:
        ql = len(Q)
        while ql:
            r,c = Q.popleft()        
            for n in range(4):
                nr = r + rr[n]
                nc = c + cc[n]

                # 자신보다 큰 물고기가 있는 칸 또는 이미 방문한 곳은 패스
                if nr < 0 or nc < 0 or nr >= len(data) or nc >= len(data[0]):
                    continue
                # 빈칸 또는 같은 크기의 물고기가 있는 칸은 지나갈 수 있음
                if visited[nr][nc] == -1:
                    if data[nr][nc] == 0 or data[nr][nc] == size:
                        visited[nr][nc] = visited[r][c] + 1
                        Q.append([nr,nc])
                    elif 1 <= data[nr][nc] < size:
                        pos.append([nr,nc])
            ql -= 1            
        if pos:
            nr,nc = min(pos)
            fish += 1                     
            # 크기가 size인 아기 상어가 물고기를 size 수만큼 먹으면 1씩 증가
            if fish == size:
                size += 1
                fish = 0
            print(pos,fish,size,nr,nc)          
            data[nr][nc] = 0
            return nr,nc,size,visited[r][c]+1,fish
    matrix_print(visited)       
    print(time)         
    sys.exit()

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
print(data)

for i in range(N):
    for j in range(N):
        if data[i][j] == 9:
            x,y = i,j    
            data[i][j] = 0

size,time,fish = 2,0,0
while True:
    x,y,size,time,fish = bfs(x,y,size,time,fish)