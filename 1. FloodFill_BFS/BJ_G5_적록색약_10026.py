# https://www.acmicpc.net/problem/10026

from collections import deque
import sys
input = sys.stdin.readline

def bfs(i,j,color):
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
            if data[nr][nc] == color and visited[nr][nc] == 0:                
                visited[nr][nc] = 1
                Q.append([nr,nc])
                if color == 'G':
                    data[nr][nc] = 'R'

N = int(input())
data = [list(input().rstrip()) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
cnt = 0
for color in ['R','G','B']:
    for i in range(N):
        for j in range(N):
            if data[i][j] == color and visited[i][j] == 0:
                bfs(i,j,color)
                if color == 'G':
                    data[i][j] = 'R'
                cnt += 1
A = cnt

visited = [[0]*N for _ in range(N)]
cnt = 0
for color in ['R','B']:
    for i in range(N):
        for j in range(N):
            if data[i][j] == color and visited[i][j] == 0:
                bfs(i,j,color)
                cnt += 1
B = cnt
print(A,B)