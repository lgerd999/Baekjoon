
import sys
from collections import defaultdict
input = sys.stdin.readline

def airplane(start):
    visited = []    
    visited.append(start)
    Q = [start]    
    cnt = 0
    while Q:
        node = Q.pop()        
        # print(node)
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                cnt += 1
                Q.append(i)
    # print(visited)
    return cnt

T = int(input())
for _ in range(T):
    graph = defaultdict(list)
    N,M = map(int,input().split())
    for _ in range(M):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)    
    
    print(airplane(1))
    
    

