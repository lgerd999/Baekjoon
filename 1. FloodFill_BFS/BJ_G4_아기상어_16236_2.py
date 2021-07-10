# https://www.acmicpc.net/problem/16236

from collections import deque
def bfs(r,c,size):
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]    
    visited = [[-1] * N for _ in range(N)]
    visited[r][c] = 0

    Q = deque()
    Q.append([r,c])
    eatable = []
    while Q:
        r,c = Q.popleft()        
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]

            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue           
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1     # 거리 계산
                if data[nr][nc] == 0 or data[nr][nc] == size:   # 데이터 위치에 0 또는 size와 같은 물고기가 있는 경우
                    Q.append([nr,nc])
                elif 0 < data[nr][nc] < size:       # 아기상어가 물고기를 먹을 수 있는 위치 저장
                    eatable.append([nr,nc,visited[nr][nc]])

    if eatable:  
        # 아기 상어가 물고기를 먹을 때 가장 가까운 거리에 있는 물고기를 선택해야 함. x[2]는 거리순, x[0]은 거리가 같고 위치가 제일 위쪽 제일 왼쪽순으로 정렬하기 위함
        eatable.sort(key=lambda x:(x[2],x[0]))            
        return eatable[0]
    return None
          

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

# 아기 상어 위치
for i in range(N):
    for j in range(N):
        if data[i][j] == 9:
            x,y = i,j
            data[i][j] = 0

size, fish,time = 2,0,0
while True:
    next_value = bfs(x,y,size)
    # 더 이상 먹을 물고기가 없는 경우 빠져나간다.
    if next_value is None:
        break
    x,y,c = next_value
    data[x][y] = 0      # 물고기를 먹으면 해당 칸은 빈칸으로 처리한다

    fish += 1
    if fish == size:
        size += 1
        fish = 0
    time += c       # 움직인 거리가 곧 시간(1칸 이동이 1초)
print(time)   
