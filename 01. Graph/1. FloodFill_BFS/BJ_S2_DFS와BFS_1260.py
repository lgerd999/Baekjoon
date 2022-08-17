# https://www.acmicpc.net/problem/1260

from collections import defaultdict,deque
import sys
input = sys.stdin.readline

'''
* DFS와 BFS 차이점
1. 초기조건
 - BFS : 방문 변수 visited의 초기 노드에 대해 방문 처리
 - DFS : 방문 변수 visited 변수만 선언
2. 반복 구조
 - BFS : 큐에 있는 노드와 연결된 노드들에 대해 방문 되어 있지 않는 경우 방문 처리하고 큐에도 추가
 - DFS : 스택에 있는 노드가 방문 이력이 있는지 확인해서 없으면 방문 처리하고, 해당 노드와 연결된 노드들을 스택에 추가
3. 알고리즘
 - BFS(너비 우선) : 시작 노드와 연결되 노드들을 전부 큐에 추가하여 방문 처리
 - DFS(깊이 우선) : 시작 노드와 연결된 노드들 중 스택에 있는 가장 빠른 노드 하나에 대해 다시 연결되어 있는 노드를 계속 방문
'''
# 스택을 이용한 반복 구조를 이용한 DFS 구현
def dfs(start):
    Q = []
    visited = []
    Q.append(start)     
    while Q:
        x = Q.pop()                
        if x not in visited:
            visited.append(x)
            # 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
            y = sorted(data[x],reverse=True)
            for i in y:
                Q.append(i)                
    print(*visited)       

# 큐를 이용한 반복 구조를 이용한 BFS 구현
def bfs(start):
    visited = []     
    Q = deque()    
    Q.append(start)
    visited.append(start)
    while Q:        
        x = Q.popleft()
        # 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
        y = sorted(data[x])
        for i in y:
            if i not in visited:                
                visited.append(i)                
                Q.append(i)
    print(*visited)
  
data = defaultdict(list)
N,M,V = map(int,input().split())
for _ in range(M):
    # 입력으로 주어지는 간선은 양방향이다
    x,y = map(int,input().split())
    data[x].append(y)
    data[y].append(x)
print(data)

dfs(V)
bfs(V)

