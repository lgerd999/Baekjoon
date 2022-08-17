# https://www.acmicpc.net/problem/5639

import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
'''
주어진 조건:
 -노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
 -노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
 -왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.
예) 50-30-24-5-28-45-98-52-60
50은 루트 노드, 그다음 30은 루트노드의 왼쪽 자식노드, 그 다음 24는 루트노드보다 크면 오른쪽 자식노드가 되고,작으면 30 자식노드의 자식 노드가 됨

1. 주어진 프리오더의 루트는 첫번째 요소이다.
2. 이후 주어진 프리오더를 탐색하다가 루트보다 커지는 첫번째 요소부터 루트의 오른쪽 트리이다.
3. 오른쪽 트리의 시작을 기준으로 나누면 한개의 프리오더는 루트 / 왼쪽트리 프리오더 / 오른쪽트리 프리오더 로 나눌 수 있다.

'''

def postorder(start,end):
    '''
    # [50, 30, 24, 5, 28, 45, 98, 52, 60]
    -(왼1) start : 0(end = 8 : 초기값), idx는 1인 위치 preorder[1] 부터 루트보다 커지는 지점인 6인 위치(preorder[6])까지 증가, idx = 6
    -(왼2) start : 1(end = 5), idx는 2인 위치 preorder[2] ~ preorder[6], idx = 5
    -(왼3) start : 2(end = 4), idx는 3인 위치 ~ 6인 위치, idx = 4 (3,4,5,6)
    -(왼4) start : 3(end = 3), idx는 4인 위치 ~ 6인 위치, idx = 3 ?, while문 조건(idx==end)으로 인해 그냥 빠져 나오게 되어 idx = 4
    -(오1) start : 4(end = 3), 그냥 return하고 오른쪽 자식 노드를 타게 됨(start,end = 3,idx = 4)
    -(왼4 return) start : 3(end = 3), idx = 4
    -(오1 return) start : 4(end = 3), return, root = preorder[3] = 5, idx = 4
    -(왼3 return)(오2) start : 2(end = 4)
    ...
    '''    
    if start > end:
        return
    root = preorder[start]   # 루트
    idx = start +1   

    # 루트를 기준으로 왼쪽과 오른쪽으로 나누는 기준
    while idx <= end:
        if preorder[idx] > root:
            break
        idx += 1   # start 가 하나씩 증가함에 따라 idx의 시작점이 다르고 이에 따라 idx 와 루트 사이의 거리를 계산
        
    print('left',start,end,'idx=',idx)    
    
    postorder(start+1,idx-1) # 루트노드의 왼쪽 자식 노드, start 가 하나씩 증가하고 idx 를 하나씩 감소   
    print('righ',start,end,'idx=',idx)
    postorder(idx,end) # 루트노드의 오른쪽 자식 노드

    print(start,end,idx,root) # 후위 순회 결과

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

print(preorder)

# 루트 부터 끝까지
# 50(루트,0)-30-24-5-28-45-98-52-60(len(preorder)-1)
postorder(0,len(preorder)-1)
