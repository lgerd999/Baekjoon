# https://www.acmicpc.net/problem/14500
# 참조: https://jeongchul.tistory.com/670 [Jeongchul]
 
tetromino = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

def find(r,c):
    ans = 0
    for i in range(len(tetromino)):
        ssum = 0        
        for n in range(4):
            nr = r + tetromino[i][n][0]
            nc = c + tetromino[i][n][1]
            if nr >= N or nc >= M:
                continue
            ssum += data[nr][nc]
        ans = max(ans,ssum)
    return ans        

sol = 0
for i in range(N):
    for j in range(M):
        sol = max(sol,find(i,j))

print(sol)