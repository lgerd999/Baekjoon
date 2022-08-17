import sys
input = sys.stdin.readline

# 노드 x가 어느 그룹에 포함되어 있는지 찾는 함수(즉, 그룹의 루트 찾기)
def find(parent,x):
    if parent[x] != x: # 루트가 아니면...
        parent[x] = find(parent,parent[x])
    return parent[x]    

# 노드 a가 포함된 그룹과 노드 b가 포함된 집합을 병합하는 함수
def union_p(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)
  if a != b:  # 두 노드가 같은 그룹이 아니면 다음 진행(만약 같다면 cycle)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

cnt = 0
while True:
    N,M = map(int,input().split())
    if N == 0 and M == 0:
        break
    # parent = [-1] * (N+1)
    parent = [i for i in range(N+1)]    
    cycle = []
    
    for _ in range(M):    
        a,b = map(int,input().split())
        # 임의의 두 노드가 같은 그룹(집합)내에 있다면, cycle 그룹에 추가.
        if find(parent,a) == find(parent,b):
            cycle.append(a)
            # break # cycle만 판별하려면 break.
        else:
            union_p(parent,a,b)   

    # 갱신 : 병합된 parent를 기준으로 각 노드의 root 찾기
    for i in range(N+1):
        find(parent, i)

    # cycle이 발생한 노드의 그룹(parent) 구하기
    group = set()
    for node in cycle:
        group.add(parent[node])
  
    answer = 0
    for i in range(1, N+1):
        if parent[i] in group: # cycle 그룹에 속한 노드는 패스!
            continue
        answer += 1    # 그룹에 속하지 않은 노드는 하나의 트리로 카운트
        group.add(parent[i])   # 새로운 그룹으로 등록

    cnt += 1
    if answer == 0:
        print(f'Case {cnt}: No trees.')
    elif answer == 1:       
        print(f'Case {cnt}: There is one tree.')
    else:
        print(f'Case {cnt}: A forest of {answer} trees.')