# https://www.acmicpc.net/problem/17086
#
'''
어떤 칸의 안전거리 = 그 칸과 거리가 가장 가까운 아기 상어와의 거리
빈칸 : 0, 상어 : 1
상하좌우대각선(8방향)을 모두 보았을 때 어떤 칸이 가지는 최대 안전거리 출력 
(-1,1),)(1,1)(-1,-1)(1,-1)

상하좌우대각선 모두 상어가 없으면 +1

아이디어 
상어(1) 위치에서 어떤칸(0)까지의 거리를 visited를 이용해 계산

0 x 1 X
X X X X
1 X 0 0
X X X X
0 0 X 1

3, 2, 1, 2 
2, 2, 2, 2 
1, 2, 3, 3 
2, 2, 2, 2 
3, 3, 2, 1


'''
import sys
# import math
from collections import deque
INF = sys.maxsize
input = sys.stdin.readline

rr = [-1,-1,-1,1, 1,1,0,0]
cc = [ 0, 1,-1,0,-1,1,-1,1]

def bfs():

    while Q:
        r,c = Q.popleft()

        for n in range(8):
            nr = r + rr[n]
            nc = c + cc[n]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if not board[nr][nc]:
                    visited[nr][nc] = visited[r][c]+1
                    Q.append((nr,nc))

    # print(visited)

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

Q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j]:
            Q.append((i,j))
            visited[i][j] = 1

bfs()
ans = 0
for i in range(N):
    ans = max(ans,max(visited[i]))
print(ans-1)