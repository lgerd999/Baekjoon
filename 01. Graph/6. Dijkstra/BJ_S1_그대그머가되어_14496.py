# https://www.acmicpc.net/problem/14496
'''
다익스트라 알고리즘 적용 : 한 노드에서 다른 노드까지의 최단경로(단, 음의 가중치는 없다)를 구할 때 사용
 - 지금까지 찾은 노드들에 연결되어 있는 간선들 중에 가중치가 가장 작은 것을 고르는 방식
 - 루트에 있는 간선들을 찾으면 그에 따른 노드들을 추가하면서 트리를 확장
트리 : 사이클이 없는 그래프, 단 방향
벨만 포드 : 음의 가중치가 있는 경우
'''
import heapq
 
def dijkstra():       
    Q = [(0,a)] # 가중치, 시작 노드       
    while Q:
        time,node = heapq.heappop(Q)    
        if dist[node] == -1:
            dist[node] = time
            for v,w in graph[node]:                 
                alt = time + w               
                heapq.heappush(Q,(alt,v))   
     
    print(dist[b])
    return
 
a,b = map(int,input().split())
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    x,y = map(int,input().split())
    graph[x].append((y,1))
    graph[y].append((x,1))
 
dist = [-1] * (N+1)
 
dijkstra()