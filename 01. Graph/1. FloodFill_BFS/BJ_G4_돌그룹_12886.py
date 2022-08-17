# https://www.acmicpc.net/problem/12886
# BFS

import sys
from collections import deque,defaultdict
input = sys.stdin.readline

def bfs():
    Q = deque()
    Q.append(data)
    visited[tuple(data)] = 1
    while Q:
        a,b,c = Q.popleft()
        
        if a==b==c:
            return 1
        
        # A,B,C 그룹의 경우의 수는 (A,B), (A,C), (B,C) 
        for x,y in ((a,b),(a,c),(b,c)):
            if x == y :
                continue
            if x < y:
                y -= x  # y를 먼저 계산해 주어야 뒤에 x 계산에 오류가 없다.
                x = 2*x                
            else:
                x = x-y # x를 먼저 계산해 주어야 뒤에 y 계산에 오류 발생하지 않음.
                y = 2*y 
            z = total - x - y    
            if not visited[(x,y,z)]:
                visited[(x,y,z)] = 1
                Q.append([x,y,z])
    return 0            

data = list(map(int,input().split()))
visited = defaultdict(int)
total = sum(data)

if total%3:
    print(0)
else:    
    print(bfs())