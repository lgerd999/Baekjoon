# https://www.acmicpc.net/problem/1012

from collections import deque
import sys
input = sys.stdin.readline

def bfs(i,j):
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]
    Q = deque()
    Q.append([i,j])
    visited[i][j] = 1
    while Q:
        r,c = Q.popleft()
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]

            if nr < 0 or nc < 0 or nr >= N or nc >= M or visited[nr][nc]:
                continue
            if bchu[nr][nc] == 1 :
                Q.append([nr,nc])
                visited[nr][nc] = 1


T = int(input())
for _ in range(T):
    N,M,K = map(int,input().split())
    visited = [[0] * M for _ in range(N)]
    bchu = [[0] * M for _ in range(N)]
    for i in range(K):
        x,y = map(int,input().split())
        bchu[x][y] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if bchu[i][j] and visited[i][j] == 0:
                bfs(i,j)
                cnt += 1
    print(cnt)                