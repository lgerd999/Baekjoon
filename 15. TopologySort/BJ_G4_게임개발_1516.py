
from collections import deque,defaultdict

# 위상 정렬 함수
def topology_sort():
    ans = [0] * (N + 1)
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            ans[i] = weight[i]

    # 큐가 빌 때까지 반복
    cnt = 0
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            ans[i] = max(ans[i], weight[i] + ans[now])
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1,N+1):                    
        print(ans[i])

N = int(input())
#data = [list(map(int,input().split())) for _ in range(N)]

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (N + 1)
weight = [0] * (N + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = defaultdict(list)

# 방향 그래프의 모든 간선 정보를 입력 받기
for i in range(1,N+1):  # i : 전입, data[1] : 전출
    data = list(map(int, input().split()))
    weight[i] = data[0]
    #if data[1] == -1: continue
    for j in data[1:-1]:
        graph[j].append(i) # 정점 A에서 B로 이동 가능
    # 진입 차수를 1 증가
        indegree[i] += 1    # 노드 a는 진출, 노드 b는 진입 차수

topology_sort()