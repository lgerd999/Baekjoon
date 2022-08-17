# https://www.acmicpc.net/problem/2573
#

import sys
from collections import deque

input = sys.stdin.readline

rr = [-1,0,1,0]
cc = [0,-1,0,1]

# def matrix_print(grid):
#     print()
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             print(grid[i][j], end=' ')
#         print()    

def bfs(i,j):
    Q = deque()
    Q.append((i,j))
    while Q:
        r,c = Q.popleft()
        
        iceland.append((r,c))
        
        for n in range(4):
            x = r + rr[n]
            y = c + cc[n]
            
            if x < 0 or y < 0 or x >= N or y >= M :
                continue
            
            if data[x][y] == 0 and data[r][c] > 0 and not visited[x][y] :
                data[r][c] -= 1
            elif data[x][y]  and not visited[x][y]:
                visited[x][y] = 1
                Q.append((x,y))

    # matrix_print(data)
    
N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

iceland = deque()

# 빙산이 있는 좌표만 별도 저장(이중 루프로 인한 시간 초과 방지 목적)
for i in range(1,N-1):
    for j in range(1,M-1):
        if data[i][j]:
            iceland.append((i,j))

cnt = 0
while True:
    split = 0
    visited = [[0]*M for _ in range(N)]     
    checked = False
       
    # 배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다.
    for x in range(len(iceland)):
        i,j = iceland.popleft()
        if data[i][j] and not visited[i][j]:
            visited[i][j] = 1
            bfs(i,j)
            split += 1        
    
    # 다 녹을때까지 분리되지 않는 경우
    if len(iceland) == 0:        
        checked = True
        break
                
    # 두 덩어리 이상으로 분리된 경우         
    if split >= 2:        
        break   
    
    # 연차 카운트
    cnt += 1           

if checked:
    print(0)    
else:    
    print(cnt)    

'''
5 7
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0

5 7
0 0 0 0 0 0 0
0 1 0 0 0 1 0
0 0 0 0 0 0 0
0 1 0 0 0 1 0
0 0 0 0 0 0 0

5 7
0 0 0 0 0 0 0
0 10 10 10 10 10 0
0 10 10 10 10 10 0
0 10 10 10 10 10 0
0 0 0 0 0 0 0
'''
    

