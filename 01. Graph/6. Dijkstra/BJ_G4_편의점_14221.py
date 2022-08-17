# https://www.acmicpc.net/problem/14221

# from heapq import heappop,heappush
# # from collections import defaultdict
# import sys
# input = sys.stdin.readline

# def dijkstra(start,end):
#     Q =[(0,start)]
#     # dist = defaultdict(int)   
#     dist = [sys.maxsize]*(N+1)     
#     dist[start] = 0
#     min_v = sys.maxsize
#     while Q:
#         weight,node = heappop(Q)
#         # if node not in dist:        
#         if dist[node] < weight:
#             continue
            
#         dist[node] = weight
#         if node in end:                                
#             if min_v > weight:
#                 min_v = weight

#         for v,w in graph[node]:            
#             alt = weight + w
#             heappush(Q,(alt,v))
#     print(dist)                
#     return min_v

# N,E = map(int,input().split())  # N : node, E : Edge
# # graph = defaultdict(list)
# graph = [[] for _ in range(N+1)]
# for _ in range(E):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))
#     graph[b].append((a,c))
# print(graph)
# p,q = map(int,input().split())
# home = list(map(int,input().split()))
# mart = list(map(int,input().split()))

# ans = sys.maxsize
# for s in home:
#     ans = min(ans,dijkstra(s,mart))
    
# print(ans)

##################################################################################
# from heapq import heappop,heappush
# from collections import defaultdict
# import sys
# input = sys.stdin.readline
# INF = sys.maxsize

# def dijkstra(start,end):
#     Q = []    
#     result = INF
#     heappush(Q,(0,start))        # start : 집, end : 편의점
#     while Q:
#         weight,node = heappop(Q)               
#         if node in home:
#             break
        
#         if dist[node] >= weight:        
#             dist[node] = weight
#             for v,w in graph[node]:
#                 alt = weight + w
#                 if dist[v] >= alt:
#                     heappush(Q,(alt,v))  
#     # 노드
#     for e in end:
#         result = min(result,dist[e])    
#     return result         
    
# N,E = map(int,input().split())  # N : node, E : Edge
# # graph = [[] for _ in range(N+1)]
# graph = defaultdict(list)
# for _ in range(E):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))
#     graph[b].append((a,c))

# p,q = map(int,input().split())
# home = list(map(int,input().split()))
# mart = list(map(int,input().split()))

# ans = INF
# for s in mart:
#     dist = defaultdict(lambda:sys.maxsize)    # 무한대로 초기 설정
#     ans = min(ans,dijkstra(s,home))     # 집에서 편의점까지 최단 거리

# print(ans)
'''
6 9
1 4 1
1 5 2
1 6 3
2 4 2
2 5 3
2 6 1
3 5 1
3 6 2
3 3
1 2 3
4 5 6
defaultdict(<class 'int'>, {1: 0, 4: 1, 5: 2, 2: 3, 3: 3, 6: 3})  
defaultdict(<class 'int'>, {2: 0, 6: 1, 4: 2, 1: 3, 3: 3, 5: 3})  
defaultdict(<class 'int'>, {3: 0, 5: 1, 6: 2, 1: 3, 2: 3, 4: 3}) 

6 9
1 4 1
1 5 2
1 6 3
2 4 2
2 5 3
2 6 1
3 4 3
3 5 1
3 6 2
3 3
3 2 1
4 5 6
'''

# 그래프에서 가중치가 있는 최단 거리 탐색 :다익트라
# 그래프에서 최단 거리 탐색 : BFS
# 31% 시간초과

import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra():    # 편의점 노드가 시작점
    q = []
    for start in store: # 편의점의 모든를 우선순위 큐에 넣어서 모든 경로에서 동시에 시작할 수 있게 함
        heapq.heappush(q, (0, start))      
             
    while q:
        weight, node = heapq.heappop(q)
        # home에 있는 노드간의 최단거리는 필요치 않음
        if node in home:
            continue

        # 큐에서 뽑아낸 거리(가중치)가 이미 갱신된 거리보다 클 경우(=방문한 셈) 무시
        if min_dists[node] < weight:
            continue
        # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for v,w in graph[node]:
            alt = weight+ w   # 시작->node거리 + node->node의인접노드 거리
            if alt < min_dists[v] and v != start:      # 집 노드까지의 최단 거리 갱신
                min_dists[v] = alt
                heapq.heappush(q, (alt, v))
            dist[v] = min(dist[v],min_dists[v]) # 각 노드별 가장 짧은 거리를 저장


n, m = map(int, input().split())    # 노드와 정점
INF = sys.maxsize
dist = [INF] * (n+1)    # 모든 경로의 최단 거리를 저장하는 리스트
min_dists = [INF] * (n+1)   # 하나의 편의점 노드에서 집 노드까지의 최단 거리를 저장    
graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

p,q = map(int, input().split()) # 시작점(집), 종료점(편의점)
home = list(map(int,input().split()))
store = list(map(int,input().split()))
    
'''
# 편의점 노드에서 집까지 최단 경로 구하기 
# 아래와 같이 구현하면 시간 초과됨(31%에서 시간초과)
for i in store:     
    min_dists = [INF] * (n+1)   # 하나의 편의점 노드에서 집 노드까지의 최단 거리를 저장
    min_dists[i] = 0    # 시작노드->시작노드 거리 기록
    dijkstra(i)     
'''
   
dijkstra()

# 편의점 노드 중 가장 최단 거리를 가지는 정점이 집 노드
min_dist = INF
ind = 0
for i in sorted(home):  # 거리가 같은 곳이 여러 군데인 경우 정점이 낮은 곳을 출력하기 위해서는 home을 정렬해야 함.             
    if min_dist > dist[i]:
        min_dist = dist[i]
        ind = i

print(ind)