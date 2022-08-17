# https://www.acmicpc.net/problem/1275
# 이 문제는 x,y 합을 구한 다음 a,b 값을 update하는 문제임.

import sys
from collections import defaultdict
input = sys.stdin.readline

def init(node,start,end):
    
    if start == end:
        tree[node] = data[start]
    else:
        init(node*2, start, (start+end)//2)
        init(node*2 + 1, (start+end)//2 + 1, end)        
        tree[node] = tree[node*2] + tree[node*2 +1]

def query(node,start,end,left,right):
    # 1. end |left    right| start
    if end < left or right < start:
        return 0
    # 2. left start end right
    if left <= start and end <= right:
        return tree[node] 
    # 3. otherwise
    return query(node*2, start, (start+end)//2, left, right) + query(node*2 + 1, (start+end)//2 +1, end, left, right)    

def update(node,start,end,idx,diff):
    # idx | left right | idx
    if idx < start or end < idx:
        return
    tree[node] += diff
    if start !=end :
        update(node*2,start,(start+end)//2, idx,diff)
        update(node*2 +1, (start+end)//2 +1, end, idx,diff)

def update_back(node,start,end,idx,val):
    # idx | left right | idx
    if idx < start or end < idx:
        return
    if start == end:
        data[idx] = val
        tree[node] = val
        return
    update_back(node*2,start,(start+end)//2, idx,val)
    update_back(node*2 +1, (start+end)//2 +1, end, idx,val)
    tree[node] = tree[node*2] + tree[node*2+1]
    

tree = defaultdict(int)

N, Q = map(int,input().split())
data = list(map(int,input().split()))
init(1,0,N-1)   # node 1(Root) : 0 ~ N-1
for _ in range(Q):
    x,y,a,b = map(int,input().split())
    if x > y:
        print(query(1,0,N-1,y-1,x-1))
    else:
        print(query(1,0,N-1,x-1,y-1))        
    diff = b - data[a-1]
    data[a-1] = b    
    update(1,0,N-1,a-1,diff)    
    # update_back(1,0,N-1,a-1,b)
    
    