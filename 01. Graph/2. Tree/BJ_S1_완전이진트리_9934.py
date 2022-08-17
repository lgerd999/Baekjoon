# https://www.acmicpc.net/problem/9934
# 완전 이진트리 : 입력 구간이 1 ~ 2^K이므로 완전 이진트리 구조이므로 Root node는 중간에 위치하게 됨.

import sys
from collections import defaultdict
input = sys.stdin.readline

# 완전 이진트리로 가운데 부모를 기준으로 왼쪽과 오른쪽 자식 노드로 분리해서 계산
def preorder(start,end,depth):
    if start == end:  #
        inorder[depth].append(building[start])
        return
    mid = (start + end)//2
    inorder[depth].append(building[mid])   
        
    preorder(start,mid-1,depth+1)
    preorder(mid+1,end,depth+1)

K = int(input())
building = list(map(int,input().split()))
inorder = [[] for _ in range(K)] # depth가 K인 K x X 행렬 생성
    
preorder(0,len(building)-1,0)

for i in inorder:
    print(*i)