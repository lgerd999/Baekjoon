# https://www.acmicpc.net/problem/1113
from collections import deque
def bfs(i,j,n):
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]
 
    visited[i][j] = 1
 
    global cnt  # 수영장에 물이 얼마만큼 높이 담을 수 있는지 체크하는 변수
    cnt = 1
    flag = 1
 
    queue = deque()
    queue.append([i,j])
    while queue:
        r,c = queue.popleft()           
        for h in range(4):
            nr = r + rr[h]
            nc = c + cc[h]
 
            if nr < 0 or nc < 0 or nr >= N or nc >= M:      
                flag = 0   # 수영장 외곽 쪽 모두 제외     
                continue
             
            if data[nr][nc] <= n and visited[nr][nc] == 0:     # 수영장 최대 높이를 넘지 않고 방문한 이력이 없다면
                cnt += 1
                visited[nr][nc] = 1
                queue.append([nr,nc])               
    if flag:       
        return cnt
    return 0              
 
N,M = map(int,input().split())
 
data =[]
level = 0
for _ in range(N):  # 수영장 최대 높이 
    data.append(list(map(int,list(input()))))   
    A = max(data[-1])   
    level = max(level,A)
 
summ = 0
for n in range(1,level):    # 수영장 물이 넘치지 않는 최대 높이까지 반복
    visited =[[0]*M for _ in range(N)]       
    count = 0
    for i in range(N):   
        for j in range(M):
            if data[i][j] <= n and visited[i][j] == 0:  # 수영장 높이보다는 낮고 방문한 이력이 없다면
                count += bfs(i,j,n)           
    summ += count          
    print(n,count)   
    '''
    입력
    3 5
    16661
    61116
    16661
    각 단계별 물을 채울 수 있는 칸의 개수
    1 3
    2 3
    3 3
    4 3
    5 3
    '''  
print(summ)