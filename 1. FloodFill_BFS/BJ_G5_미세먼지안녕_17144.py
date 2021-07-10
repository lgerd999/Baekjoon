# https://www.acmicpc.net/problem/17144

from collections import deque
def matrix_print(grid):
    print()
    for i in range(len(grid)):
        for j in grid[i]:
            print(j,end='  ')
        print()    

def bfs(i,j):        
    rr = [-1,1,0,0] # 상,하,좌,우
    cc = [0,0,-1,1]

    Q = deque()  
    Q.append([i,j])  
    
    while Q:        
        r,c = Q.popleft()        
        cnt = 0
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]

            if nr < 0 or nc < 0 or nr >= R or nc >= C or data[nr][nc] == -1:
                continue            
            cnt += 1
            visited[nr][nc] += data[i][j]//5
        visited[r][c] += data[r][c] - (data[r][c]//5)*cnt

def cleanup(x):	# 청소기 윗부분 처리
    rr = [0, -1, 0, 1]		# 청소 진행방향 우, 상, 좌, 하
    cc = [1, 0, -1, 0]

    now = visited[x][1]	# 첫번째 청소할 구역의 먼지 기록
    visited[x][1] = 0		# 첫번째 구역 청소 
    d = 0	# 방향
    nr = x
    nc = 1
    while True:
        nr += rr[d]
        nc += cc[d]
        next = visited[nr][nc]	# 청소 예정 구역의 먼지 기록
        visited[nr][nc] = now	# 청소 (앞에서 가져온 먼지 저장)
        now = next	# next에서 기록한 먼지를 다음에 쓰기 위해 now로 옮김
        if nr + rr[d] < 0 or nr + rr[d] > x or nc + cc[d] < 0 or nc + cc[d] >= C:	#  다음 좌표를 미리 계산해서 방향을 바꿀지 여부 판단
            '''
            nr + rr[d] < 0 : 상
            nr + rr[d] > x : 하
            nc + cc[d] < 0 : 좌
            nc + cc[d] >= C :우
            '''
            d += 1
        if d == 4:	# 모든 방향을 청소했을 때
            break

def cleandown(x):	# 청소기 아랫부분 처리
    rr = [0, 1, 0, -1]	# 청소 진행방향 우, 하, 좌, 상
    cc = [1, 0, -1, 0]
								# cleanup 함수와 동일. (방향 바꾸기 처리만 다름)
    now = visited[x][1]
    visited[x][1] = 0
    d = 0
    nr = x
    nc = 1
    while True:
        nr += rr[d]
        nc += cc[d]
        next = visited[nr][nc]
        visited[nr][nc] = now
        now = next
        if nr + rr[d] < x or nr + rr[d] >= R or nc + cc[d] < 0 or nc + cc[d] >= C:
            '''
            nr + rr[d] < x : 상
            nr + rr[d] >= R :하
            nc + cc[d] < 0 : 좌
            nc + cc[d] >= C :우
            '''
            d += 1
        if d == 4:
            break

R,C,T = map(int,input().split())
data =[list(map(int,input().split())) for _ in range(R)]
#print(data)


for t in range(T):    
    visited = [[0] * C for _ in range(R)]
    Cl = []
    for i in range(R):
        for j in range(C):
            if  data[i][j] == -1:
                Cl.append([i,j]) 
                continue
            elif data[i][j] == 0:
                continue
            else:
                bfs(i,j)
    #matrix_print(visited)
    
    cleanup(Cl[0][0])
    cleandown(Cl[1][0])

    visited[Cl[0][0]][0] = -1
    visited[Cl[1][0]][0] = -1
    data = visited
    #matrix_print(visited)

answer = 0
for i in range(R):
    for j in range(C):
        answer += data[i][j]
print(answer+2)        