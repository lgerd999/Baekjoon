import sys
sys.setrecursionlimit(300000)
def dfs(i,j):
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]

    data[i][j] = 0
    global cnt
    cnt += 1

    for n in range(4):
        nr = i +rr[n]
        nc = j +cc[n]

        if nr < 0 or nr >= len(data) or nc < 0 or nc >= len(data[0]) or data[nr][nc] != 1:        
            continue
        dfs(nr,nc)
    
    return cnt

N = int(input())
data = [list(map(int,input())) for _ in range(N)]
# print(data)
# N = 7
# data = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]

cnt,ans = 0,0
result = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 1:
            result.append(dfs(i,j))
            cnt = 0            
            ans += 1

result.sort()
print(ans)
print(*result,sep='\n')
