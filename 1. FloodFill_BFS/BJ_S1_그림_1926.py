# https://www.acmicpc.net/problem/1926

import sys
sys.setrecursionlimit(3000000)
   
def dfs(i,j):    
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]

    data[i][j] = 0
    
    global area
    area += 1

    for n in range(4):
        nr = i + rr[n]
        nc = j + cc[n]

        if nr < 0 or nc < 0 or nr >= len(data) or nc >= len(data[0]) or data[nr][nc] != 1:
            continue
        
        dfs(nr,nc)
        
    return area #len(pos)    


readline = sys.stdin.readline
n,m = map(int,readline().split())
data = [list(map(int,readline().split())) for _ in range(n)]
# print(data)
# n,m = 6,5
# data =[[1, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]

cnt = 0            
ans = 0
area = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 1:                
            ans = max(ans,dfs(i,j))    
            area = 0              
            cnt += 1            
print(cnt)
print(ans)


#print(*picture(data),sep ='\n')

'''
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
'''