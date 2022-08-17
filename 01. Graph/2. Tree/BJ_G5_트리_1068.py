# https://www.acmicpc.net/problem/1068


import sys
from collections import defaultdict
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)

def node(i):
    global cnt
    
    if root == D: # 루트 노드가 삭제된다면, 리턴
        return
    if len(G[i]) == 0: # 리프노트라면, 카운팅하고 리턴
        cnt += 1
        return
    for j in range(len(G[i])):
        # 부모노드에 자식 노드 하나만 있는 경우가 아닌 경우만 패스
        # 자식 노드만 체크하게 되면 삭제되는 순간 부모 노드가 리트 노드가 되고 카운트도 하지 않고 종료되는 문제가 있음.
        if G[i][j] == D and len(G[i]) != 1:    
            continue
        node(G[i][j])
        # print()
  
N = int(input())
L = list(map(int,input().split())) # 라인 단위로 입력
D = int(input())   # 삭제 노드
cnt = 0

G = defaultdict(list)

for i in range(N):
    # 루트 노드 구하기
    if L[i] == -1:
        root = i
    # 인접 리스트 생성
    G[L[i]].append(i) 

node(root)

print(cnt)
'''
트리가 왼쪽 자식노드만 존재하는 경우, 즉 루트 노드부터 일직선인 경우에 대한 반례.
4
-1 0 1 2
2
ans = 1
'''