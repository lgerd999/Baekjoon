# https://www.acmicpc.net/problem/14442
# 벽이 K개
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]
    visited = [[[0] * (M) for _ in range(N)] for _ in range(K+1)]   #visited[2][N][M]

    visited[0][0][0] = 1
    Q = deque()
    Q.append([0,0,0])
    # cnt = K - 1
    while Q:
        r,c,w = Q.popleft()        

        if r == N - 1 and c == M - 1:        
            return visited[w][r][c]            
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]

            if nr < 0 or nc < 0 or nr >= len(data) or nc >= len(data[0]) :
                continue

            # 벽을 만나 벽을 뚫는 상황            
            if data[nr][nc] == '1' and w < K and visited[w+1][nr][nc] == 0:  # 이동할 방향에 대해 벽이 있고, 현 위치 기준 w = 0인 경우, 즉 벽을 뚫고 온 경우에 대해 계산                
                print('1 ',w,r,c,':',visited[w][r][c])
                visited[w+1][nr][nc] = visited[w][r][c] + 1
                Q.append([nr,nc,w+1])                
                
            # 벽을 만나지 않은 상황    
            elif data[nr][nc] == '0' and visited[w][nr][nc] == 0:                    
                visited[w][nr][nc] = visited[w][r][c] + 1
                Q.append([nr,nc,w])
    # print(visited)            
    return -1
    

N,M,K = map(int,input().split())
data = [list(input()) for _ in range(N)]

# print(data)
print(bfs())