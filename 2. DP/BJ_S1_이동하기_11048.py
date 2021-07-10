# https://www.acmicpc.net/problem/11048

N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

rr = [1,1,0]
cc = [0,1,1]
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = max(visited[i][j],data[i][j]) 
        for n in range(3):
            nr = i + rr[n]
            nc = j + cc[n]

            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            visited[nr][nc] = max(visited[nr][nc],visited[i][j] + data[nr][nc])        
print(visited[N-1][M-1])      
