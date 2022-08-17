# https://www.acmicpc.net/problem/2357
# 최소값과 최대값을 구분하는 변수 사용 불가 : 메모리 제약

import sys
from math import ceil,log2
input = sys.stdin.readline

def init(node,start,end):
    if start == end:
        # tree[node] = arr[start]
        tree[node][0] = arr[start]
        tree[node][1] = arr[start]
    else:
        init(node*2,start,(start+end)//2)    
        init(node*2 +1, (start+end)//2 +1,end)
        tree[node][0] = min(tree[node*2][0], tree[node*2 +1][0])
        tree[node][1] = max(tree[node*2][1], tree[node*2 +1][1])
        
def query_min(node,start,end,left,right):
    # end left right start, 아무 관련 없은 경우
    if end < left or start > right:
        # 최소값을 구할 때 0을 return하면 오류가 발생할 수 있음. 주어진 문제에서 모든 정수값은 1이상 1,000,000,000 이하의 값을 갖음.
        return -1   # -1값은 나올 수 없는 값
    # left start end right, 완전 포함되는 경우
    if left <= start and end <= right:
        return tree[node][0]
    else:    
        lmin = query_min(node*2, start, (start+end)//2,left,right)
        rmin = query_min(node*2 +1, (start+end)//2 +1, end,left,right)
        # 왼쪽 또는 오른쪽 노드 값이 -1이라는 의미는 이 구간은 최소값을 구하지 말고 패스하라는 의미임.
        if lmin == -1:               
            return rmin
        elif rmin == -1:            
            return lmin
        else:
            return min(lmin,rmin)

def query(node,start,end,left,right):
    # end left right start, 아무 관련 없은 경우
    if end < left or start > right:        
        return 0   # 
    # left start end right, 완전 포함되는 경우
    if left <= start and end <= right:
        return tree[node][1]
    else:    
        lmin = query(node*2, start, (start+end)//2,left,right)
        rmin = query(node*2 +1, (start+end)//2 +1, end,left,right)        
        return max(rmin,lmin)


N,M = map(int,input().split())
arr = list(int(input()) for _ in range(N))

h = ceil(log2(N))
size_tree = 1 << (h+1)
tree = [[0] * 2 for _ in range(size_tree)]
# print(tree)
init(1,0,N-1)
# print(tree)

for i in range(M):
    a,b = map(int,input().split())    
    print(query_min(1,0,N-1,a-1,b-1),end=' ')
    print(query(1,0,N-1,a-1,b-1))