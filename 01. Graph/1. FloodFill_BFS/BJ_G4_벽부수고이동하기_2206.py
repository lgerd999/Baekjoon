# https://www.acmicpc.net/problem/2206
# 참조 : https://pacific-ocean.tistory.com/348

from collections import deque
import sys

readline = sys.stdin.readline
N,M = map(int,readline().split())
data = [list(map(int,readline().strip())) for _ in range(N)]
# print(data)
# N,M = 6,4
# data = [[0, 1, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]
 
def bfs():
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]
    visited = [[[0] * (M) for _ in range(N)] for _ in range(2)]   #visited[2][N][M]

    visited[0][0][0] = 1
    Q = deque()
    Q.append([0,0,0])
    while Q:
        r,c,w = Q.popleft()        
        if r == N - 1 and c == M - 1:
            return visited[w][r][c]            
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]

            if nr < 0 or nc < 0 or nr >= len(data) or nc >= len(data[0]) :
                continue

            # visited[w][x][y]         
            #  - w : 0 - 벽을 뚫은 경우, 1 - 벽을 뚫지 않은 경우

            # 벽을 만나 벽을 뚫는 상황
            if data[nr][nc] == 1 and w == 0 : # 이동할 방향에 대해 벽이 있고, 현 위치 기준 w = 0인 경우, 즉 벽을 뚫고 온 경우에 대해 계산
                visited[1][nr][nc] = visited[0][r][c] + 1
                Q.append([nr,nc,1])
                
            # 벽을 만나지 않은 상황    
            elif data[nr][nc] == 0 and visited[w][nr][nc] == 0:                    
                visited[w][nr][nc] = visited[w][r][c] + 1
                Q.append([nr,nc,w])
    return -1

print(bfs())
             