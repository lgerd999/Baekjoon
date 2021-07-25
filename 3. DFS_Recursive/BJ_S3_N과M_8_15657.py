# https://www.acmicpc.net/problem/15657

import sys
input = sys.stdin.readline

def dfs(path):
    if len(path) > M:
        return

    if len(path) == M:        
        result.append(path)
        return
    
    for i in range(N):        
        if path and path[-1] > num[i] : # 비내림 차순 A1 <= A2 <= ... <= Ak
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