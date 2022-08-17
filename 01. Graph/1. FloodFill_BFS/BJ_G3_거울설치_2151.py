# https://www.acmicpc.net/problem/2151
#

'''
문('#')은 항상 2개(입구/출구)
거울 설치는 45 도 방향
'.'은 빛이 통과할 수 있고, '!'는 거울 설치할 장소, '*'은 벽

아이디어
1. 거울 45도 설치 좌표 : 대각선 상하좌우 (1,1),(1,-1),(-1,1),(-1,-1)로 생각했는데 빛의 성질을 고려하지 않은 틀린 이해였다.
  (올바른 이해) 
    --> 거울을 45도 방향으로 틀면 빛은 수직(90도)방향으로 꺾인다.
    --> 꺾이는 방향은 주어지지 않았기 때문에 최적의 방향으로 선택해 주면 된다.
    --> 상하좌우 (-1,0),(1,0),(0,-1),(0,1) 이동하면서 !를 만나면 90도로 위치 변경(반사)할 수 있다.
    --> 거울을 꺾는 방향 이동은 아래와 같이 나타낼 수 있다.
        - 우선 방향은 [↑0 ↓1 ←2 →3 ] 으로 둔다.
        - 위쪽(0) 방향은 왼쪽(2)이나 오른쪽(3)으로 꺾인다. [ 0 → 2 ,0 → 3 ]
        - 아래쪽(1) 방향은 왼쪽(2)이나 오른쪽(3)으로 꺾인다. [1 → 2 , 1 → 3 ]
        - 왼쪽(2) 방향은 위쪽(0)이나 아래쪽(1)으로 꺾인다. [ 2 → 0 , 2 → 1 ]
        - 오른쪽(3) 방향은 위쪽(0)이나 아래쪽(1)으로 꺾인다. [3 → 0 , 3 → 1 ]

2. 문(입구)에서 상하좌우 이동하면서 거울 설치 좌표('!')가 있는지 확인해서 있으면 Q에 추가(방향도 추가) 및 방문 기록
 - visited[x좌표][y좌표][이동방향]
 - 거울을 만났을 때 거울을 추가하거나 추가하지 않을 수 있다.
 - 즉, 방향을 직진(거울 추가 X), +90(거울 추가), -90(거울 추가)방향으로 꺽는 3가지 좌표를 큐에 추가한다. 
 - Count 변수
 - Q에 추가시 거울이 반사할 수 있는 4가지 방향 탐색  
 - 빛은 직진성이 있으니 '.'을 만나면 방향성 유지 및 count 유지
4. 상하좌우에 문(출구)이 있는지 체크해서 있으면 종료하고 count를 출력 

***#*
*.!.*
*!.!*
*.!.*
*#***
2

'''
import sys
from collections import deque
input = sys.stdin.readline

# rr = [1,1,-1,-1]
# cc = [1,-1,1,-1]
rr = [-1,1,0,0]
cc = [0,0,-1,1]

changeDir = ((2, 3), (2, 3), (0, 1), (0, 1))

# def matrix_print(A):
#     for i in range(N):
#         for j in range(N):
#             print(A[i][j]

def bfs():
    while Q:
        # d = 방향
        r,c,d = Q.popleft()
        
        # if r == x[1]  and c == y[1]:
        #     print(visited[r][c][d])

        # 큐에 들어 있는 방향으로 계속 탐색(빛의 직진성)
        # for n in range(4):
        nr = r + rr[d]
        nc = c + cc[d]
        if 0 <= nr < N and 0 <= nc < N and home[nr][nc] != '*':
            if home[nr][nc] == '!':
                # 거울 미설치 - 통과
                if visited[nr][nc][d] == -1:
                    visited[nr][nc][d] = visited[r][c][d]
                    Q.append((nr,nc,d))
                else:
                    if visited[nr][nc][d] > visited[r][c][d] :
                        visited[nr][nc][d] = visited[r][c][d]
                        Q.append((nr,nc,d)) 
                # 거울 설치        
                for nd in range(changeDir[d][0],changeDir[d][1]+1):
                    if visited[nr][nc][nd] == -1:
                        visited[nr][nc][nd] = visited[r][c][d] + 1
                        Q.append((nr,nc,nd))
                    else:
                        if visited[nr][nc][nd] > visited[r][c][d] + 1 :
                            visited[nr][nc][nd] = visited[r][c][d] + 1
                            Q.append((nr,nc,nd)) 
                
            elif home[nr][nc] == '.':
                if visited[nr][nc][d] == -1:
                    visited[nr][nc][d] = visited[r][c][d]
                    Q.append((nr,nc,d))
                else:
                    if visited[nr][nc][d] > visited[r][c][d] :
                        visited[nr][nc][d] = visited[r][c][d]
                        Q.append((nr,nc,d))   
    result = sys.maxsize
    for ans in visited[x[1]][y[1]]:
        if ans != -1:
            result = min(result,ans)
    return result
    # print(visited[x[1]][y[1]])
    # print(home)
                       


N = int(input())
home = [list(input().rstrip()) for _ in range(N)]
# print(home)
#거울 설치 방향 고려해서 3차원 배열
visited = [[[-1]*4 for _ in range(N)] for _ in range(N)]

# 출입문의 위치
x,y = [],[]
for i in range(N):
    for j in range(N):
        if home[i][j] == '#':
            x.append(i)
            y.append(j)
            home[i][j] = '.'
# print(x,y)

# 입구에서 상하좌우 방향들을 큐에 넣기
Q = deque()
for i in range(4):
    nr = x[0] + rr[i]
    nc = y[0] + cc[i]
    if 0 <= nr < N and 0 <= nc < N and home[nr][nc] != '*':
        Q.append((x[0],y[0],i))
        visited[x[0]][y[0]][i] = 0

print(bfs())            