# https://www.acmicpc.net/problem/2263

import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# preorder : 루트-왼쪽-오른쪽
def preorder(in_start,in_end,post_start,post_end):
    # start와 end가 같은 지점은 루트 노드와 마지막 노드일 때
    if (in_start > in_end) or (post_start > post_end):
        return
    
    # postorder의 마지막 노드가 root노드(부모노드)
    root = postorder[post_end]
    print(root,end=' ')
    
    # graph[root]가 루트 노드의 인덱스이므로 여기서 왼쪽 리프노드까지의 거리가 left가 됨
    # right는 마지막 인덱스에서 루트노드 인덱스까지의 거리가 됨
    left = graph[root] - in_start
    right = in_end - graph[root]
    print('\n',left,right,'input=',N,in_start,in_end,post_start,post_end)
    
    # left와 right로 나누어 preoder 진핻
    preorder(in_start, in_start+left-1, post_start, post_start+left-1) # 왼쪽 자식
    preorder(in_end-right+1, in_end, post_end-right, post_end-1) # 오른쪽 자식


N = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

graph = defaultdict(int)

# inorder : 왼쪽-루트-오른쪽, 루트를 기점으로 왼쪽과 오른쪽의 자식 노드 개수를 알 수 있음.
# postorder의 마지막 노드가 inorder의 어느 index에 위치해 있는지 확인을 위해 inorder 값들을 graph에 저장.
# 조금더 설명하자면, 아래는 indorder의 제일 처음 시작하는 노드가 왼쪽의 리프 노드라는 점과 postorder에서 
# 루트 노드를 알고 있다는 점을 고려하여 왼쪽 노드 부터 인덱스를 0부터 시작해서 마지막까지 N-1까지
# 인덱스를 부여한다.
# 예를 들어, inorder로 1 2 3이 들어오고 post order로 1 3 2가 들어오면, 루트 노드는 2라는 점과 
# 왼쪽 리트노드가 1이라는 점을 알 수 있음
# 왼쪽 리프 노드부터 인덱스 0부터 시작하면 루트 노드는 인덱스 1을 갖고 마지막 노드는 2를 갖음
for i in range(N):
    graph[inorder[i]] = i      # inorder의 첫번째 노드는 왼쪽 노드의 리프 노드
print(graph)    

preorder(0,N-1,0,N-1)



