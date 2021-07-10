# https://www.acmicpc.net/problem/2638
from collections import deque
def matrix_print(A):
    for i in range(len(A)):
        for j in A[i]:
            print(j,end='' )
        print()    
    print()    

def bfs(i,j):
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]    
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1

    Q = deque()
    Q.append([i,j])
    while Q:
        r,c = Q.popleft()        
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]

            if nr < 0 or nc < 0 or nr >= len(cheese) or nc >= len(cheese[0]):
                continue           

            if not visited[nr][nc]: # 방문 전
                if cheese[nr][nc] >= 1: #치즈값이 1 이상이면 공기중에 노출되는 면이 있다는 의미
                    cheese[nr][nc] += 1 # 치즈 숙성도 증가
                else:                
                    visited[nr][nc] = 1
                    Q.append([nr,nc])
        
    matrix_print(cheese)        
    #matrix_print(visited)

N,M = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(N)]
#print(cheese)
ans = 0
while True:
    bfs(0,0)
    cht = 0
    for i in range(N):
        for j in range(M):
            if cheese[i][j] >= 3:   # 치즈값이 3이상인 것은 공기중에 인접한 면이 2개 이상을 의미
                cheese[i][j] = 0    # 2개면 이상 노출시 녹은 것으로 설정
                cht = 1
            elif cheese[i][j] == 2: # 치즈값이 2이면 공기중에 노출된 면이 1개 의미
                cheese[i][j] = 1    # 이는 아직 녹지 않았으므로 다시 1로 설정    
    if cht:
        ans += 1
    else:
        break
print(ans)        

'''
반례1 output = 3
9 9
0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0
0 1 0 0 0 0 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 0 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 0 0 0 0 1 0
0 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0
'''
