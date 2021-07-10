
from collections import defaultdict
def find_parent(x):
    if x == parent[x]: return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x,y):
    x,y = find_parent(x),find_parent(y)
    if x != y:
        parent[y] = x

N = int(input())
M = int(input())
city = [list(map(int,input().split())) for _ in range(N)]
connect = list(map(int,input().split()))
parent = defaultdict(int)
for i in range(1,N+1):
    parent[i] = i

for i in range(1,N+1):
    for j in range(1,N+1):
        if city[i-1][j-1] :          
            union_parent(i,j) 
ans = set()    
for i in connect:
    ans.add(find_parent(i))  
print("YES" if len(ans) == 1 else "NO")                   