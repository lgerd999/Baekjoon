# https://www.acmicpc.net/problem/1717

from collections import defaultdict
def find_parent(x):
    if x == parent[x]: return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x,y):
    x,y = find_parent(x), find_parent(y)
    if x!=y:
        parent[y] = x

ans = []
n,m = map(int,input().split())      
parent = defaultdict(int)  
for i in range(1,n+1):
    parent[i] = i
for _ in range(m):
    c,a,b = map(int,input().split())
    if c == 0:
        union_parent(a,b)
    else:
        if find_parent(a) == find_parent(b):
            ans.append("YES")            
        else:
            ans.append("NO")
print(*ans, sep='\n')            