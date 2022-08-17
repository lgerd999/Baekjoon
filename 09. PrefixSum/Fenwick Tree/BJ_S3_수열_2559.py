# https://www.acmicpc.net/problem/2559
# 누적합, 펜윅트리

import sys
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize

def query(i):
    ans = 0
    while i > 0 :
        ans += tree[i]
        i -= i & -i 
    return ans        

def update(i,num):
    while i <= N:        
        tree[i] += num
        i += (i & -i)
    return tree

N,K = map(int,input().split())
array = list(map(int,input().split()))
tree = defaultdict(int)

for i in range(N):
    tree = update(i+1,array[i])

# print(tree)

ans = -INF
i = 0
# for i in range(N-K):
while i+K <= N:    
    print(ans)
    ans = max(ans, query(i+K) - query(i))
    i += 1
print(ans)        
