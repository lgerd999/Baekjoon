# https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline

def find_parent(x):
    if x == parent[x]: return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x,y):
    x,y = find_parent(x),find_parent(y)
    if x < y :
        parent[y] = x
    else:
        parent[x] = y

N,M = map(int,input().split())  # 노드, 간선

# 부모 노드 리스트 초기화
parent = [i for i in range(N+1)]

for _ in range(M):
    u,v = map(int,input().split())

    if find_parent(u) != find_parent(v):
        union_parent(u,v)    
 
ans = set()
for i in range(1,N+1):
    ans.add(find_parent(i))        

print(len(ans))
