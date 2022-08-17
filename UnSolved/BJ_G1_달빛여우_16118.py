# https://www.acmicpc.net/problem/16118

from heapq import heappush,heappop
from collections import defaultdict
import sys

input = sys.stdin.readline

def dijkstra(graph,mod):
    Q = [(0,1)] # 여우와 늑대는 1번 그루터기에 살고 있으므로 1번부터 출발    
    dist = defaultdict(int)
    cnt = 0
    while Q:
        weight, node = heappop(Q)
        if node not in dist:
            
            dist[node] = weight

            for v,w in graph[node]:    
                if mod:
                    if cnt % 2 == 0:
                        w = w*4                        
                else:
                    w = w*2
                alt = weight + w
                heappush(Q,(alt,v))
        cnt += 1                
    print(dist)                

N,M = map(int,input().split())
graph = defaultdict(list)
for _ in range(M):
    a,b,d = map(int,input().split())
    graph[a].append((b,d))
    #graph[b].append((a,d))
dijkstra(graph,0)    # fox
dijkstra(graph,1)    # wolf