# https://www.acmicpc.net/problem/1753
from collections import defaultdict
import heapq
import sys

'''
시작 노드 K에서 각 노드까지의 최소 거리를 출력하는 문제
K= 1  dist = {1: 0, 2: 2, 3: 3, 4: 7})
1->1 : 0, 1-> 2 : 2, 1 ->3 : 3, 1 -> 4 : 7, 1 -> 5 : 없음(INF)

'''

def dijkstra(data,K):
    graph = defaultdict(list)
    for u,v,w in data:
        graph[u].append((v,w))        
    
    Q=[(0,K)]        
    dist = defaultdict(int)

    while Q:
        weight,node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = weight            
            for v,w in graph[node]:
                alt = weight + w
                heapq.heappush(Q,(alt,v))                                      
    print(dist)    
    for i in range(1,V+1):
        if i in dist.keys():
            print(*[dist[i] ], sep='\n')
        else :    
            print('INF')
    return         

input = sys.stdin.readline
V,E = map(int,input().split())  # 노드 V와 간선 E
K = int(input())    # 시작 노드
data = [list(map(int,input().split())) for _ in range(E)]

dijkstra(data,K)
