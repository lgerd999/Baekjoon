
from collections import deque

# 인접리스트
graph = { 1: [2, 5, 9], 
          2: [1, 3], 
          3: [2, 4], 
          4: [3], 
          5: [1, 6, 8], 
          6: [5, 7], 
          7: [6], 
          8: [5], 
          9: [1, 10], 
          10: [9] 
        }

def dfs_recursive(graph,start):
    visited=[]
    visited.append(start) 
        
    for node in graph[start]:
        if not visited[node]:           
            dfs_recursive(graph,node,visited)
    return visited   
   
def dfs_stack(graph,start):
    Q, visited=[],[]
    Q.append(start)
    while Q:
        node = Q.pop()
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                Q.append(i)
    return visited    

# 인접리스트
graph = { 1: [2, 3, 4], 
          2: [1, 5], 
          3: [1, 6, 7], 
          4: [1, 8], 
          5: [2, 9], 
          6: [3, 10], 
          7: [3], 
          8: [4], 
          9: [5], 
          10: [6] 
        }

def bfs_queue(graph, start):
    visited = []
    Q = deque([start])
    
    while Q:    
        node = Q.popleft()        
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                Q.append(i)
    return visited        

# 인접행렬
graph = [[1, 1, 1, 1, 0, 0],
         [1, 1, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 0, 1]] 

def dfs_stack_adj_matrix(graph,start,end):
    visited = [0] * len(graph)
    Q = []
    Q.append([start,end])
    
    while Q:
        node = Q.pop()
        for i,j in graph[node]:
            if graph 

                