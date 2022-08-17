# https://www.acmicpc.net/problem/2589
# 최단 거리를 구하기

import sys
from collections import deque
input = sys.stdin.readline

'''
# 아래 순서로 진행하면 10%에서 오답처리됨.
rr = [-1,1,0,0]
cc = [0,0,-1,1]
'''
rr = [-1, 0, 1, 0]
cc = [0, 1, 0, -1]

def matrix_print(grid):
    print()
    for i in range(len(grid)):
        for j in grid[i]:
            print(j,end=' ')
        print()  
   
def bfs(i,j):
    global dist
    # global cordinate
    
    Q = deque()
    Q.append((i,j,0))
        
    while Q:
        r,c,w = Q.popleft()
        
        if w > dist:
            dist = w
            cordinate.append((r, c))                  
                     
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]
            
            if nr < 0 or nc < 0 or nr >= L or nc >= W or nr >= 50 or nc >= 50 or island[nr][nc] == 'W':
                continue
            
            if island[nr][nc] == 'L' and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] +1                
                Q.append((nr,nc,visited[nr][nc]))                           
    
    # matrix_print(visited) 
        

L,W = map(int,input().split())
island = [list(input().rstrip()) for _ in range(L)]

cordinate =[]
dist = 0

visited = [[0]*W for _ in range(L)]
for i in range(L):    
    for j in range(W):
        if island[i][j] == 'L' and not visited[i][j]:                        
            visited[i][j] = 1 
            bfs(i,j)
    
        # matrix_print(visited)

ans = 0
for x in range(len(cordinate)):    
    r, c = cordinate[x][0],cordinate[x][1]
    # print(r,c)
    dist = 0
    visited = [[0] * W for _ in range(L)]
    visited[r][c] = 1
    bfs(r, c)
    if ans < dist:
        ans = dist

print(ans-1)

'''
# pypy로 실행시아래 코드도 정답 

import sys
from collections import deque
input = sys.stdin.readline

rr = [-1,1,0,0]
cc = [0,0,-1,1]

def matrix_print(grid):
    print()
    for i in range(len(grid)):
        for j in grid[i]:
            print(j,end=' ')
        print()  
   
def bfs(i,j):
    global dist
    visited[i][j] = 1
    Q = deque()
    Q.append([i,j,0])
    cnt = 0
    
    while Q:
        r,c,w = Q.popleft()
        
        if w > dist:
            dist = w
            cordinate.append((r, c))
        
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]
            
            if nr < 0 or nc <0 or nr >= L or nc >= W or nr >= 50 or nc >= 50 or island[nr][nc] == 'W':
                continue
            
            if island[nr][nc] == 'L' and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] +1                
                Q.append([nr,nc,visited[nr][nc]])           
                if cnt < visited[nr][nc]:
                    cnt = visited[nr][nc]
    # 거리    
    # matrix_print(visited)
    # return cnt-1

L,W = map(int,input().split())
island = [list(input().rstrip()) for _ in range(L)]
# print(island)

cordinate =[]
dist = 0

ans = -1
for i in range(L):    
    for j in range(W):
        visited = [[0]*W for _ in range(L)]
        if island[i][j] == 'L':            
            # print(i,j)
            # ans = max(ans, bfs(i,j))          
            bfs(i,j)  

# print(ans)        
print(len(cordinate))
'''