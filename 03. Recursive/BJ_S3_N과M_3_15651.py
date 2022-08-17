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

'''
4 2

1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
'''    