# https://www.acmicpc.net/problem/6118
#

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs():
    Q = deque()
    Q.append(1)
    visited[1] = 1
    while Q:
        r = Q.popleft()        
        for i in graph[r]:
            if not visited[i]:
                Q.append(i)
                visited[i] = visited[r] + 1
    # print(visited)            

N,M = map(int,input().split())
graph = defaultdict(list)
visited = [0]*(N+1)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

bfs()    

m = max(visited)        
print(visited.index(m),m-1,visited.count(m))       
        