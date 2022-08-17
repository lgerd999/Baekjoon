# https://www.acmicpc.net/problem/1520
# https://velog.io/@nathan29849/BAEKJOON-1520-%EB%82%B4%EB%A6%AC%EB%A7%89-%EA%B8%B8-DFS-BFS-python

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(r,c):
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]
    
    # 도착 좌표에 도달하면, 1을 리턴
    if r == M-1 and c == N-1:
        return 1
    
    # 이미 방문한 곳이면
    if visited[r][c] != -1:
        return visited[r][c]
    
    # 방문하지 않은 경우   
    visited[r][c] = 0
           
    for n in range(4):
        nr = r + rr[n]
        nc = c + cc[n]        
                
        if nr < 0 or nc < 0 or nr >= M or nc >= N:
            continue
        
        # 기준 좌표의 값보다 높이가 낮은 곳의 값이 작으면, 기준 좌표의 값에 높이가 낮은 곳의 값을 더함
        if data[nr][nc] < data[r][c]:                
            visited[r][c] += bfs(nr,nc)              # 리턴된 값의 합이 경로의 수
           
    return visited[r][c]

M,N = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(M)]
visited = [[-1]*N for _ in range(M)]
# print(data)

print(bfs(0,0))