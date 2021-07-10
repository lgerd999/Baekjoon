# https://www.acmicpc.net/problem/1967
'''
시간 복잡도 개선
 - 기존 다익스트라 템플릿에서 시간 복잡도가 늘어날 만한 부분을 함수에서 제외
 - Root에서 마지막 노드까지 경로와 가중치를 체크하여 가중치가 최대가 되는 Node를 계산

문제 해결 알고리즘
 - 루트에서 마지막 노드까지 가중치가 가장 큰 노드를 구함
 - 가중치가 가장 큰 노드에서 다시 한번 BFS/다익스트라 알고리즘 적용

참고 : 트리(무방향 그래프)로 두 노드간 경로가 유일하므로 가중치 유무와 상관없는 BFS로 구현
- 다익스트라 알고리즘 복잡도 O(NlogN)이며, N번 수행시 O(N^2logN) : 간선의 가중치가 동일하지 않는 경우
- BFS 알고리즘 복잡도 O(N), N번 수행시 O(N^2) : 간선의 가중치가 동일한 경우 사용
'''
from collections import defaultdict
import heapq

def dijkstra(graph,N,K):        
    Q = [(0,K)]        
    dist = defaultdict(int)
    max_w,max_n = 0,0
    while Q:
        weight,node = heapq.heappop(Q)                
        if node not in dist:
            dist[node] = weight
            if max_w < weight:
                max_w = weight
                max_n = node       
                print(weight,node)           
            for v,w in graph[node]:
                alt = weight + w
                heapq.heappush(Q,(alt,v))    
    if len(dist)== N:        
        return max_w,max_n
    return -1

N = int(input())
data = [list(map(int,input().split())) for _ in range(N-1)]

# 시간 복잡도 개선을 위해 N번 반복되는 부분을 1번으로 실행하게 하기 위해 함수에서 제외함
graph = defaultdict(list)
for u,v,w in data:
    graph[u].append((v,w))    
    graph[v].append((u,w))    

# 1번 노드에서 마지막 노드까지 최대 가중치를 갖는 노드를 구함
weight,node = dijkstra(graph,N,1)
print(node)
# 최대 가중치를 갖는 노드에서 다시 한번 알고리즘을 진행하여 가장 멀리있는 노드를 구함
weight,node = dijkstra(graph,N,node)
print(weight)
