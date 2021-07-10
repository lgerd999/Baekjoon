# https://www.acmicpc.net/problem/2668
from collections import deque,defaultdict
'''
1 2 3 4 5 6 7
3 1 1 5 5 4 6

-> 3: [1], 1: [2, 3], 5: [4, 5], 4: [6], 6: [7]
-> 노드1과 노드3, 노드 5는 사이클 관계
-> 이 문제는 사이클을 찾는 문제

'''
def bfs(V):
    visited = []
    Q = deque()
    Q.append(V)
    visited.append(V)
    while Q:
        x = Q.popleft()
        for i in data[x]:
            if i not in visited:
                visited.append(i)
                Q.append(i)
            else:
                result.append(i)
    print(visited,result,sep='\n')

def dfs(V):
    visited = []
    Q = []
    Q.append(V)    
    while Q:
        x = Q.pop()
        if x not in visited:
            visited.append(x)
            for i in data[x]:
                Q.append(i)
        else:
            result.append(i)

N = int(input())
data = defaultdict(list)
for i in range(N):
    num = int(input())
    data[num].append(i+1)    
print(data)

# 각 노드에서 사이클 찾기
result = []
for i in range(1,N+1):
    # bfs(i)
    dfs(i)

# 출력
print(len(result))
for i in result:
    print(i)
   
