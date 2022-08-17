#
#
'''

'''

import sys
input = sys.stdin.readline

rr = [-1,1,0,0]
cc = [0,0,-1,1]

def dfs():
    stack = []
    stack.append((i,j))    
    while stack:
        r,c = stack.pop()
        
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] visited[r][c] + 1:
                    visited[nr][nc] = visited[r][c] + 1
    

N,M = map(int,input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]


for i in range(N):
    for j in range(M):
        

