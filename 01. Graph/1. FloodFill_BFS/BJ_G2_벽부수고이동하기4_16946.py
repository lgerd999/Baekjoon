# https://www.acmicpc.net/problem/16946
#
'''

'''
from sys import stdin
from collections import deque
input = stdin.readline

rr = [-1,1,0,0]
cc = [0,0,-1,1]

def bfs(i,j):
    Q = deque()
    visited[i][j] = 1    
    Q.append((i,j))
    ones = set()
    cnt = 1
    while Q:
        r,c = Q.popleft()
    
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]
            
            if 0<= nr < N and 0 <= nc < M and not visited[nr][nc] :           
                visited[nr][nc] = 1        # 모두 방문한 것으로 간주.                 
                if data[nr][nc] == '0':   
                    cnt += 1                               
                    Q.append((nr,nc))
                else:
                    # 자기 자신을 더하기 위해 결과 변수에 1을 넣어 줄 용도로 사용하였으나, 틀린 답으로 출력됨.
                    # if not result[nr][nc]:
                    #     result[nr][nc] = 1
                    ones.add((nr,nc))    
    
    for x,y in ones:
        visited[x][y] = 0           # 1인 경우 상하좌우로 만나는 위치가 같은 그룹일 경우 중복 덧셈을 하게 되는데 이를 방지하기 위해 
        result[x][y] += cnt
        # result[x][y] %= 10        # 이렇게 사용하면 틀렸습니다로 출력됨.
        if result[x][y] >= 10: 
            result[x][y] %= 10
        
    # print(result,ones,cnt)

N,M = map(int,input().split())
data = [list(input().rstrip()) for _ in range(N)]
result = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]    

# 자기 자신값을 더하기 위해 아래와 같이 미리 1의 값을 입력해 줌.
for i in range(N):
    for j in range(M):
        if data[i][j] == '1':
            result[i][j] = 1

for i in range(N):
    for j in range(M):
        if data[i][j] == '0' and not visited[i][j]:
            bfs(i,j)

for i in result:
    # print(*i, sep='')
    print(''.join(map(str,i)))  # 이렇게 사용하는 것이 약 100ms 시간을 줄이는 효과가 있음.