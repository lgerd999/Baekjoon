# https://www.acmicpc.net/problem/1707
# union-find 알고리즘으로 풀려고 했는데, 이분 그래프 정의에 의해 cycle이 있어도 이분 그래프가 되는 경우가 있어 이 알고리즘으로 푸는것은 실패함.
'''
이분 그래프 : 그래프 노드의 집합을 둘로 나눴을 때, 각 집합에 속한 노드끼리는 서로 인접하지 않도록 분할할 수 있는 그래프
'''

import sys
from collections import deque,defaultdict
input = sys.stdin.readline

def bfs(start):
    if visited[start] == 0:
        visited[start] = 1
    Q = deque()
    Q.append(start)
    while Q:
        node = Q.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                Q.append(i)
                if visited[node] == 1:   
                    visited[i] = 2
                else:
                    visited[i] = 1   
            elif visited[node] == visited[i]:
                
                return False
    return True            

T = int(input())
for _ in range(T):
    V,E = map(int,input().split())
    graph = defaultdict(list)     
    visited = [0] * (V+1)
    for _ in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    flag = 0    
    for i in range(1,V+1):
        ans = bfs(i)
        if not ans:
            flag = 1
            break

    # print(visited,flag)

    if flag:
        print('NO')
    else:
        print('YES')      