# https://www.acmicpc.net/problem/1504

from collections import defaultdict
import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline
def dijkstra(data,Start,End):
    Q = [(0,Start)]
    dist = defaultdict(int)
    while Q:
        distance, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = distance
            if node == End:
                return dist[node]
            for v,w in data[node]:
                alt = distance + w
                heapq.heappush(Q,(alt,v))
    #print(dist)
    return INF
graph = defaultdict(list)
N, E = map(int,input().split())
for i in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
v1,v2 = map(int,input().split())    
case1 = dijkstra(graph,1,v1) + dijkstra(graph,v1,v2) + dijkstra(graph,v2,N)
case2 = dijkstra(graph,1,v2) + dijkstra(graph,v2,v1) + dijkstra(graph,v1,N)
ans = min(case1,case2)
print(case1,case2,ans)
print(ans if ans < INF else -1)
