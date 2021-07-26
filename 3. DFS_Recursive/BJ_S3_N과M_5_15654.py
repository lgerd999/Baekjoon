# https://www.acmicpc.net/problem/15654

import sys
input = sys.stdin.readline

def dfs(path):
    if len(path) > M:
        return

    if len(path) == M:
        result.append(path)
        return
    
    for i in range(N):
        if num[i] not in path:            
            dfs(path+[num[i]])            
            
    return result

result = []
N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()

ans = dfs([])
for i in ans:
    print(*i) 

'''
4 2
9 8 7 1

1 7
1 8
1 9
7 1
7 8
7 9
8 1
8 7
8 9
9 1
9 7
9 8
'''    