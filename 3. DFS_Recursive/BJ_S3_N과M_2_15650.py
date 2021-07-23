# https://www.acmicpc.net/problem/15650

def dfs(index,path):    
    if len(path) == M:
        result.append(path)
    for i in range(index,N+1):
        dfs(i+1,path+[i])
    
    return result
result = []
N,M = map(int,input().split())

ans = dfs(1,[])
for i in ans:
    print(*i)

