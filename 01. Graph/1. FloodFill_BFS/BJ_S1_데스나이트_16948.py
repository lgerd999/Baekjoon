# https://www.acmicpc.net/problem/16948
#

import sys
from collections import deque
input = sys.stdin.readline

rr = [-2,-2,0,0,2,2]
cc = [-1,1,-2,2,-1,1]

def bfs():
    Q = deque()
    Q.append((r1,c1))
    visited[r1][c1] = 1
    while Q:
        r,c = Q.popleft()
        
        if r == r2 and c == c2:            
            return visited[r][c] - 1
        
        for n in range(6):
           x = r + rr[n] 
           y = c + cc[n]
           if x < 0 or y < 0 or x >= N or y >= N:
               continue
           
           if not visited[x][y]:
                visited[x][y] = visited[r][c]+1
                Q.append((x,y))
        #    else:
        #        # 방문했더라도 원래 값보다 더 작다면,
        #        if visited[x][y] > visited[r][c] +1:
        #         visited[x][y] = visited[r][c]+1
        #         Q.append((x,y))
                        
    return -1

N = int(input())
r1,c1,r2,c2 = map(int,input().split())
visited = [[0]*N for _ in range(N)]
print(bfs())

