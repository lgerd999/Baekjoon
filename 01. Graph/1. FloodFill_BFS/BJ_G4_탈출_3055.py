# https://www.acmicpc.net/problem/3055
#
'''
'*' : 물이 차 있는 곳
'.' : 비어 있는 곳
'X' : 돌
'D' : 비버의 굴
'S' : 고슴도치 위치

매 분마다 비어 있는 칸으로 물이 확장한다. 물이 있는 칸과 인접해 있는 비어 있는 칸은 물이 차게 된다.
물과 고슴도치는 돌을 통과할 수 없고, 고슴도치는 물로 차 있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.

고슴도치가 안전하게 비버의 굴로 이동하기 위한 최소한의 시간 구하기.

고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다.


'''

import sys
from collections import deque

input = sys.stdin.readline

rr = [-1,1,0,0]
cc = [ 0,0,-1,1]

def matrix_print(A):
    for i in range(R):
        for j in range(C):
            print(A[i][j],end=' ')
        print()    

def bfs(i,j):
    # Q = deque()
    Q.append((i,j))
    visited[i][j] = 1
    while Q:
        # 고슴도치 이동
        q = len(Q)  # 상하좌우 큐에 들어 있는 위치들 수
        while q:
            r,c = Q.popleft()

            for n in range(4):
                nr = r + rr[n]
                nc = c + cc[n]
                # 이전 위치가 돌이 아니고 물이 아니어야 함.
                if 0 <= nr < R and 0 <= nc < C and board[r][c] != 'X' and board[r][c] != '*' and not visited[nr][nc]:
                    if board[nr][nc] == '.' :
                        visited[nr][nc] = visited[r][c] + 1
                        Q.append((nr,nc))
                    elif board[nr][nc] == 'D':
                        # matrix_print(visited)
                        # print()
                        # matrix_print(board)
                        print(visited[r][c])
                        return 
            q -= 1

        # 물의 이동
        wq = len(WQ)
        while wq:
            wr,wc = WQ.popleft()
            for n in range(4):
                nr = wr + rr[n]
                nc = wc + cc[n]
                # 돌은 피해가야 함.
                if 0 <= nr < R and 0 <= nc < C and board[wr][wc] != 'X':
                    if board[nr][nc] == '.' :
                        board[nr][nc] = '*'
                        WQ.append((nr,nc))
            wq -= 1

    # matrix_print(visited)
    # print()
    # matrix_print(board)
    print("KAKTUS")
    return 


R,C= map(int,input().split())
board = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

Q,WQ = deque(),deque()

#고슴도치,물 위치 찾기
for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            a,b = i,j
            # board[i][j] = '.'
        elif board[i][j] == '*':
            WQ.append((i,j))

bfs(a,b)