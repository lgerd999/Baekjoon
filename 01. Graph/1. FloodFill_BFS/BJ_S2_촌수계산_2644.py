import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def dfs(start,end):
    visited = defaultdict(list)
    visited[start] = 1
    Q = deque()
    Q.append(start)
    dist = defaultdict(int)
    while Q:
        node = Q.pop()
        
        for i in graph[node]:            
            if not visited[i]:       
                dist[i] = dist[node] + 1
                Q.append(i)
                visited[i] = 1
    if dist[end]:
        print(dist[end])
    else:
        print(-1)    

graph = defaultdict(list)                

N = int(input())
S, E = map(int,input().split())
M = int(input())
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(S,E)