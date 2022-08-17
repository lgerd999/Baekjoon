# https://www.acmicpc.net/problem/16437

from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(v):     
    # leaf 노드이고 양 이라면,
    if v not in node.keys():        
        return node[v] if node[v] > 0 else 0

    # leaf 노드가 아니고, 양에 대해서 합산
    result = 0 if node[v] < 0 else node[v]
    for i in edge[v]:
        result += dfs(i)
    #print(result)
    # 늑대섬을 지날 때에 대해 차감
    if node[v] < 0:
        if result > abs(node[v]): # 늑대 개체수보다 클 경우
            result += node[v]
            node[v] = 0
        else:               # 늑대 개체수보다 작을 경우
            node[v] += result
            result = 0
    return result            

node = defaultdict(int)
edge = defaultdict(list)
N = int(input())
node[1] = 0
for i in range(1,N):    
    t,a,p = input().split()    
    edge[int(p)].append(i+1)        
    if t == 'S':               
        node[i+1] = int(a)
    else:                
        node[i+1] = -int(a)
#print('***1=',node,edge,sep='\n')
print(dfs(1))

'''
늑대는 지나갈때마다 잡아 먹는게 아니라 평생 최대 한마리만 잡아 먹음.
7
W 10 1
W 40 2
W 10 2
S 100 3
S 50 3
S 20 4
ans = 110
'''