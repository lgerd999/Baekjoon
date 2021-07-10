# https://www.acmicpc.net/problem/1766

import heapq
import sys
input = sys.stdin.readline

# 노드와 간선의 개수 입력
N,M = map(int,input().split())

# 모든 노드에 대한 진입차수 초기화
indegree = [0]*(N+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(N+1)]

# DAG의 모든 간선 정보 입력 받기
for _ in range(M):
    a,b = map(int,input().split())    
    graph[a].append(b) 
    indegree[b] += 1

def topology_sort():
    result = []
    q = []

    for i in range(1,N+1):
        if indegree[i] == 0:
            heapq.heappush(q,i)
    while q:
        now = heapq.heappop(q)            
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q,i)
    for i in result:
        print(i,end=' ')

topology_sort()

'''
5 4
4 1
5 1
2 5
3 5

'''