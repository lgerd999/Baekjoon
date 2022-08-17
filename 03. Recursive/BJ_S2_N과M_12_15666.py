# https://www.acmicpc.net/problem/15666

import sys
input = sys.stdin.readline

def dfs(path):
    if len(path) > M:
        return

    if len(path) == M:      
        if path in result:
            return  
        result.append(path)
        return
    
    for i in range(N):            
        if path and num[i] < path[-1] :
            continue
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
9 7 9 1

1 1
1 7
1 9
7 7
7 9
9 9
'''