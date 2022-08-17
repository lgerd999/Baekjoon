import sys
sys.setrecursionlimit(2499)
def number_island(data):
    def dfs(i,j):
        # rr = [-1,-1,-1,1,0,0,1,1]
        # cc = [-1,1,0,0,-1,1,-1,1]
        if i < 0 or j < 0 or i >= len(data) or j >=len(data[0]) or data[i][j] != 1:
            return

        data[i][j] = 0

        dfs(i,j-1)
        dfs(i,j+1)
        
        dfs(i-1,j)
        dfs(i-1,j-1)
        dfs(i-1,j+1)                     
        
        dfs(i+1,j)
        dfs(i+1,j-1)
        dfs(i+1,j+1)
    
    cnt = 0    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 1:
                dfs(i,j)
                cnt += 1
    return cnt

w,h = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(h)]
#print(data)

ans = []
while w and h:
    ans.append(number_island(data))
    w,h = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(h)]

for i in range(len(ans)):
    print(ans[i])