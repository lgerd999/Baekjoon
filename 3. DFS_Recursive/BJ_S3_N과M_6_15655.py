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

'''
4 2
9 8 7 1

1 7
1 8
1 9
7 8
7 9
8 9
'''    