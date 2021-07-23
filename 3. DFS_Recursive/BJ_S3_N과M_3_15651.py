# https://www.acmicpc.net/problem/15651

def dfs(path):        
    if len(path) == M:        
        result.append(path)
    if len(path) > M:
        return
    for i in range(1,N+1):
        dfs(path+[i])
    
    return result
result = []
N,M = map(int,input().split())

ans = dfs([])
for i in ans:
    print(*i)