# https://www.acmicpc.net/problem/15655

import sys
input = sys.stdin.readline

def dfs(index,path):
    if len(path) > M:
        return

    if len(path) == M:        
        result.append(path)
        return
    
    for i in range(index,N):
        dfs(i+1,path+[num[i]])                
            
    return result

result = []
N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()

ans = dfs(0,[])
for i in ans:
    print(*i) 