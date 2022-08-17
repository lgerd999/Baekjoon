# https://www.acmicpc.net/problem/1261
#
'''
이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 
현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성

'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs():   
    rr = [1,0,-1,0]
    cc = [0,1,0,-1]

    visited = [[-1]* N for _ in range(M)] 
    visited[0][0] = 0
    Q = deque()
    Q.append([0,0])
    while Q:
        r,c = Q.popleft()
        
        # print(visited)        
    
        for n in range(4):
            nr = rr[n] + r
            nc = cc[n] + c
            
            if nr < 0 or nc < 0 or nr >= len(data) or nc >= len(data[0]) or visited[nr][nc] != -1:
                continue
            
            # 벽이 있다면, visited에 벽을 부순 횟수 증가
            if data[nr][nc] == 1 :                
                visited[nr][nc] = visited[r][c] + 1
                Q.append([nr,nc])
            # 벽이 없다면, visited 이전 값과 동일
            elif data[nr][nc] == 0:
                visited[nr][nc] = visited[r][c]
                Q.appendleft([nr,nc])    # 벽을 부수지 않고 지나가는 것으 우선 순위가 높음
    
    # print(visited)        
    return visited[M-1][N-1]
            

N,M = map(int,input().split())
data = [list(map(int,input().rstrip())) for _ in range(M)]

print(bfs())