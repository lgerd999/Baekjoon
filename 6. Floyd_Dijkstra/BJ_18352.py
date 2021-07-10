from collections import defaultdict
import heapq
def dijkstra(times,K,X):
    graph = defaultdict(list)

    for u,v,w in times:
       graph[u].append((v,w))
       #graph[v].append((u,w))
    Q = [(0,X)]
    dist = defaultdict(int)
    result=[]
    while Q:
        time,node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            if dist[node] == K:                
                result.append(node)

            for v,w in graph[node]:
                alt = time + w
                heapq.heappush(Q,(alt,v))
        #print(dist)
    if not result:
        result.append(-1)
    return result

N,M,K,X = map(int,input().split())
data = [list(map(int,input().split()))+[1] for _ in range(M)]
# print(data)

# N,M,K,X = 4,4,2,1
# data = [[1, 2, 1], [1, 3, 1], [2, 3, 1], [2, 4, 1]]

print(*dijkstra(data,K,X),sep='\n')
