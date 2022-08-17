# https://www.acmicpc.net/problem/1600
# BFS
'''
말이 갈 수 있는 좌표
(-2,1),(-1,2),(-1,-2),(-2,-1),(2,1),(1,2),(1,-2),(2,-1)
원숭이는 K번 말처럼 움직일 수 있음(즉, 기회를 잘 보아서 움직여야 함)
말은 장애물(1)을 뛰어 넘을 수 있지만, 원숭이는 그렇지 못함.
시작점에서 도착지점까지의 최소한의 동작 횟수를 구하는 문제.

아이디어
1. 말과 원숭이가 갈 수 있는 좌표를 정의하고 말이 갈수 있는 좌표를 카운팅하여 0이 되면 원숭이 좌표만
이동할 수 있도록 구현.
2. visited 변수는 3차원으로 정의하여 XY좌표+횟수로 지정하고 횟수는 K로 초기화한다.
3. visited 시작점은 (0,0,K) 위치로 방문 여부를 나타낸다면 1이 맞지만, 여기서는 카운팅을 목적으로
하기 때문에 0으로 유지한다.

'''
import sys
from collections import deque

input = sys.stdin.readline

hx = [-2,-2,-1,-1,1,1,2,2]
hy = [-1,1,-2,2,-2,2,-1,1]
rr = [-1,1,0,0]
cc = [0,0,-1,1]

def bfs():
    Q = deque()
    Q.append((0,0,K))
    visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
    # visited[0][0][K] = 1

    while Q:
        r,c,cnt = Q.popleft()
        if r == H-1 and c == W-1:
            # print(visited)
            return visited[r][c][cnt]

        if cnt > 0:    
            # 말의 움직임
            for h in range(8):
                dx = r + hx[h]
                dy = c + hy[h]
                if 0 <= dx < H and 0 <= dy < W and not visited[dx][dy][cnt-1]:
                    if not board[dx][dy]:
                        visited[dx][dy][cnt-1] = visited[r][c][cnt] + 1
                        Q.append((dx,dy,cnt-1))

        # 원숭이의 움직임    
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]
            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc][cnt]:
                if not board[nr][nc]:
                    visited[nr][nc][cnt] = visited[r][c][cnt] + 1
                    Q.append((nr, nc,cnt))
    return -1

K = int(input())
W,H = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(H)]

# print(board)
print(bfs())