# https://www.acmicpc.net/problem/2606
from collections import deque,defaultdict

N = int(input())
P = int(input())
data = [list(map(int,input().split())) for _ in range(P)]

def bfs(node):
    visited = []
    visited.append(node) 
    Q = deque()
    Q.append(node)
    while Q:
        n = Q.popleft() 
        for i in graph[n]:
            if i not in visited:
                visited.append(i)
                Q.append(i)
    #print(visited)
    return visited

graph = defaultdict(list)
for u,v in data:
    graph[u].append(v)
    graph[v].append(u)
#print(graph)    
print(len(bfs(1))-1)