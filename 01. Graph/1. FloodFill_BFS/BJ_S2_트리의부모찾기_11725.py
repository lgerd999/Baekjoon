# https://www.acmicpc.net/problem/11725
# 전형 적인 BFS 알고리즘 적용
import sys
from collections import defaultdict,deque
input = sys.stdin.readline

def bfs(start):
    visited = defaultdict(list)
    visited[start] = 1  # 탐색한 노드는 1로 표기
    Q = deque()
    Q.append(start)
    while Q:
        node = Q.popleft()                
        for i in graph[node]:            
            if not visited[i]:
                ans[i] = node  # ans의 key에 자식 노드의 정보를 넣고, value값에 부모 노드 정보를 저장
                Q.append(i)
                visited[i] = 1
   
graph = defaultdict(list)
ans = defaultdict(list)
N = int(input()) # 

# 간선 정보를 바탕으로 인접 딕셔너리로 변환
for i in range(N-1):
    i,j = map(int,input().split())
    graph[j].append(i)
    graph[i].append(j)

# 노드1(루트)에서 그래프 탐색(노드 0은 미사용)
bfs(1)

# 부모 노드 출력(노드 2부터)
for i in range(2,len(ans.keys())+2):
    print(ans[i])


