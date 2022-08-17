# https://www.acmicpc.net/problem/16928
# BFS

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    Q = deque()
    Q.append(1)
    # visited[1] = 0
    
    while Q:
        r = Q.popleft()                         
        
        # 주사위는 1 ~ 6 범위
        for n in range(1,7):
            nr = r + n            
            if nr > 100:
                continue
            # 점프 위치
            nr = next[nr]
            
            if not visited[nr]:
                visited[nr] = visited[r]+1
                Q.append(nr)
    # print(visited)                
    return visited[100]          

N,M = map(int,input().split())
visited = [0]*(101)    

# 점프 위치 초기화
next = [i for i in range(101)]

# 뱀과 사다리의 점프 위치는 모두 next 변수에 저장
for i in range(N):
    x,y = map(int,input().split())
    next[x] = y

for i in range(M):
    x,y = map(int,input().split())
    next[x] = y

print(bfs())