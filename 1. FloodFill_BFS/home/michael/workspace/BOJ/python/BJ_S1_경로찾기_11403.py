# https://www.acmicpc.net/problem/11403
# 알고리즘 : 플로이드 마샬 또는 그래프 탐색(BFS,DFS)
# 플로이드 마샬 알고리즘 : 모든 정점에 대한 경로를 계산하는 알고리즘
'''
문제의 이해
- 입력(i:row, j:col) : 간선
3
0 1 0
0 0 1
1 0 0
==> i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻
    : 1행은 2열, 2행은 3열, 3행은 1열
    : 노드 1 --> 2 --> 3 --> 1
    : 노드1에서 노드1로 오는 경우는 1-->2-->3-->1, 노드2에서 노드2로 오는 경우는 2-->3-->1-->2
    : 결국 모두 1로 출력됨선
 - 출력 : 인접 행렬
1 1 1
1 1 1
1 1 1
==> 1행 1열이 1인 의미 : 노드1에서 노드1로 오는 경로가 있다는 의미임
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):  
    while Q:
        next = Q.popleft()  # 노드 next 는 출발 노드
        for i in range(N):  # 노드 i는 도착 노드
            if visited[x][i] == 0 and G[next][i] : # 방문 기록이 없고, 간선이 있다면
                Q.append(i) # 도착 노드를 Q에 추가                
                visited[x][i] = 1   

N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
Q = deque()
visited = [[0] * N for _ in range(N)]

# 각 노드에 대해 경로 탐색
for i in range(N):
    Q.append(i) # 출발 노드
    bfs(i)

for j in visited:
    print(*j)


