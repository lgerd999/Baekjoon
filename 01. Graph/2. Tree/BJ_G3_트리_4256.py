import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def postorder(pre_start,pre_end,in_start,in_end):
    if (pre_start > pre_end) or (in_start > in_end):
        return
    root = preorder[pre_start]    

    left = graph[root] - in_start
    right = in_end - graph[root]

    # postorder(in_start,in_start + left -1, pre_start ,pre_start + left -1)
    # postorder(in_end - right +1,in_end, pre_end - right, pre_end-1)
    postorder(pre_start+1, pre_start + left, in_start,in_start+left-1)
    postorder(pre_end - right +1 , pre_end, in_end-right+1,in_end)
    print(root,end=' ')


T = int(input())
for _ in range(T):
    n = int(input()) #노드 개수
    graph = defaultdict(int)
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))
    
    for i in range(n):
        graph[inorder[i]] = i
    
    postorder(0,n-1,0,n-1)
    print()