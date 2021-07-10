# https://www.acmicpc.net/problem/15649

def dfs(path):  
    #print(path)            
    if len(set(path)) < len(path):
        return
    if len(path) > m:
        return
    if len(path) == m:
        result.append(path)          
    # if len(path) == m:
    #     if len(set(path)) == m:
    #         result.append(path)
    #     return 
    
    for i in range(1,n+1):
        dfs(path+[i])

    return result    
result = []
n,m = map(int,input().split())
for i in dfs([]):
    print(*i)
