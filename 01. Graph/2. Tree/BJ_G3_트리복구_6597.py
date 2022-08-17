import sys
from collections import defaultdict
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

def postorder(pre_s,pre_e,in_s,in_e):
    if (pre_s > pre_e) or (in_s > in_e):
        return
    root = preorder[pre_s]
    
    left = graph[root] - in_s
    right = in_e - graph[root]

    postorder(pre_s+1,pre_s+left,in_s,in_s+left-1)
    postorder(pre_e-right+1,pre_e,in_e-right+1,in_e)
    print(root,end='')    


while True:
    try:
        preorder,inorder = map(str,input().split())        
        graph = defaultdict(int)
        for i in range(len(inorder)):
            graph[inorder[i]] = i        
        postorder(0,len(preorder)-1,0,len(inorder)-1)
        print()
    except:
        break