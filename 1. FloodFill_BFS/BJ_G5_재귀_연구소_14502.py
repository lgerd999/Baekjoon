# https://www.acmicpc.net/problem/14502

import sys
import copy
from collections import deque

def matrix_print(grid):
    print()
    for i in range(len(grid)):
        for j in grid[i]:
            print(j,end=' ')
        print()    

def bfs():  # 함수 목적 : 바이러스 확산
    global ans
    w = copy.deepcopy(data) # 바이러스 확산 전 데이터 백업
#    print(data,w)
    for i in range(N):
        for j in range(M):
            if w[i][j] == 2: # 바이러스 위치 보관
                q.append([i, j])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + rr[i]
            nc = c + cc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if w[nr][nc] == 0:  # 바이러스 확산
                    w[nr][nc] = 2
                    q.append([nr, nc])

    cnt = 0
    for i in w: # 바이러스에 살아남은 안전영역 개수
        cnt += i.count(0)
    ans = max(ans, cnt)

'''
재귀함수를 통해서 데이터가 0인 부분에 대해 3개의 벽을 치는 모든 경우의 수를 계산하는 함수
wall이 3번 스택에 쌓이며 3번째 
예)
1. Stack( Wall(0,1)->1, Wall(0,2)->1   )
   Wall(0,3)-> 1로 변경하고 BFS진행 return하면 (0,3) -> 0로 변경
   (0,6)->1로 변경하고 BFS진행 .... 마지막 (6,6) -> 1로 변경하고 BFS 진행
2. 3번재 Wall 함수 return 2번째 Wall(0,2) -> 0으로 바꾸고 3번째 Wall(0,3)->1을 Stack에 넣음
   Wall(0,6)부터 (6,6)까지 BFS 진행
3. Wall함수 3개를 이용하여 모든 경우의 수 계산

'''
def wall(x):
    if x == 3:
        bfs()
        return
    for i in range(N):      # 0인 부분을 하나씩 벽을 쳐봄
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                wall(x+1)
                data[i][j] = 0
    
    #matrix_print(data)

rr = [-1, 1, 0, 0]
cc = [0, 0, -1, 1]
ans = 0

N, M = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q = deque()
wall(0)
print(ans)