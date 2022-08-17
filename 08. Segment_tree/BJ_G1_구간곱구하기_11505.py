# https://www.acmicpc.net/problem/11505
# segment tree 알고리즘 

import sys
from math import ceil,log2
from collections import defaultdict
input = sys.stdin.readline

def init(node, start, end):
    # 리프 노드인 경우
    if start == end:
        tree[node] = graph[start]        
    # 구간 곱       
    else:
        init(node*2,start,(start+end)//2)
        init(node*2 +1, (start+end)//2 +1,end)
        tree[node] =  tree[node*2] * tree[node*2+1] %1000000007
        
    
def query(node,start,end,left,right):
    if start > right or end < left:
        return 1
    
    if start >= left and end <= right:
        return tree[node]
    else:
        return query(2*node,start,(start+end)//2,left,right) * query(2*node + 1,(start+end)//2 + 1,end,left,right) %1000000007


def update(node,start,end,idx,val):
    if start > idx or end < idx:
        return        
    # 리프 노드까지 재귀 호출
    if start == end:
        graph[idx] = val  # 해당 위치의 값을 업데이트
        tree[node] = val  # 
        return
    
    update(node*2, start, (start+end)//2, idx, val)
    update(node*2 +1 , (start+end)//2 +1, end, idx, val)
    tree[node] = tree[node*2] * tree[node*2 +1] %1000000007
        
# N : 개수, M: 수의 변경이 일어난 횟수, K: 구간의 곱을 구하는 횟수
N,M,K = map(int,input().split())
graph =[]

# tree의 depth 계산 --> defaultdict으로 대체
# h = ceil(log2(N))   # depth
# tree_size = 1 << (h+1)  # 2^(h+1)
# tree = [0] * tree_size
tree = defaultdict(int)

for _ in range(N):
    graph.append(int(input()))

init(1,0,N-1)

for _ in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        update(1,0,N-1,b-1,c)        
    elif a == 2:
        print(query(1,0,N-1,b-1,c-1))    

