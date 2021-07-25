# https://www.acmicpc.net/problem/15652

def dfs(index,path):      
    if len(path) == M:                      
        result.append(path)

    if len(path) > M:        
        return        

    for i in range(index,N+1):
        dfs(i,path+[i])
    
    return result
result = []
N,M = map(int,input().split())

ans = dfs(1,[])
for i in ans:
    print(*i) 