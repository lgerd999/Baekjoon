import sys
from math import ceil,log2
input = sys.stdin.readline

def init(node,start,end):
    if start == end:
        tree[node] = S[start]
    else:    
        init(node*2,start,(start+end)//2)
        init(node*2 + 1,(start+end)//2 +1,end)
        tree[node] = tree[node*2] + tree[node*2 +1]    
    

def query(node,start,end,left,right):
    if end < left or start > right:
        return 0
    if start >= left and end <= right:
        return tree[node]
    else:    
        return query(2*node,start,(start+end)//2,left,right) + query(2*node + 1,(start+end)//2 + 1,end,left,right)
        

def update(node,start,end,idx,diff):
    if start > idx or end < idx:
        return        
    tree[node] += diff
    if start != end:
        update(node*2, start, (start+end)//2, idx, diff)
        update(node*2 +1 , (start+end)//2 +1, end, idx, diff)

def update2(node,start,end,idx,val):
    if start > idx or end < idx:
        return        
    if start == end:
        S[node] = val
        tree[node] = val
        return
    update(node*2, start, (start+end)//2, idx, diff)
    update(node*2 +1 , (start+end)//2 +1, end, idx, diff)
    tree[node] = tree[node*2] + tree[node*2 +1]

# N : 수의 개수, M : 수의 변경이 일어나는 횟수, K : 구간의 합을 구하는 횟수
N,M,K = map(int,input().split())        
S = []
for _ in range(N):
    S.append(int(input())) 

# tree = [0]*(2**(ceil(log2(N))+1)-1)
h = ceil(log2(N))
tree_size = 1 << (h+1)
tree = [0] * tree_size
# print(2**(ceil(log2(N))+1)-1)

init(1,0,N-1)

for _ in range(M+K):
    # a가 1인경우, b번째 수를 c로 변경
    # a가 2인경우, b번째 수부터 c번째 수까지 합을 구함
    a,b,c = map(int,input().split())
    if a == 1:
        diff = c - S[b-1]
        S[b-1] = c
        update(1,0,N-1,b-1,diff)
    elif a == 2:
        # b에서 c까지 구간 합
        print(query(1,0,N-1,b-1,c-1))