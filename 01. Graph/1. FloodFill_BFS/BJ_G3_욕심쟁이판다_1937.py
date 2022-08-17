# https://www.acmicpc.net/problem/1937
# 판다가 상하좌우 이동할 곳 중 가장 큰 곳으로 이동할 수 있는데 가장 오래 이동할 경우의 수를 구하는 문제
'''
주요 알고리즘
1. 상하좌우 중 가장 큰 곳만 저장하고 있으면 됨(DP). 즉, 이동할 칸 +1과 현재까지 이동한 곳의 값 중 최대값만 저장.
2. 중복 탐색을 생략하기 위해 이동할 위치의 값에 0이 아닌 값이 있으면 이미 탐색된 위치로 판단해서 더 이상 탐색하지 않음. 
 즉, 이동할 곳의 값이 있다는 것은 이전에 이미 상하좌우 탐색이 완료된 상태라는 의미.
3. DFS를 사용하면 가장 큰 값만 가지는 곳을 선택해서 이동할 수 있음

비슷한 유형 : https://www.acmicpc.net/problem/1520 내리막길

BFS로 구현시 시간초과(넓이위주 탐색)
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

rr = [-1,0,1,0]
cc = [0,1,0,-1]

def dfs(i,j):
    # 이미 탐색된 위치라면 그냥 해당 위치의 값을 리턴.
    if visited[i][j]:
        return visited[i][j]  
    
    visited[i][j] = 1   
    for k in range(4):
        x = i + rr[k]
        y = j + cc[k]
        
        if x < 0 or y < 0 or x >= n or y >= n:
            continue
        
        if data[x][y] > data[i][j] : 
            # 현 위치 DP값과 상하좌우 DP 값 중 가장 큰 위치만 현 위치에 저장
            visited[i][j] = max(visited[i][j], dfs(x,y) + 1)
    
    # print(visited)        
    return visited[i][j]                    
    
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
visited = [[0]*n for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:                                    
            ans = max(ans, dfs(i,j))
# print(visited)
print(ans)        
    
            