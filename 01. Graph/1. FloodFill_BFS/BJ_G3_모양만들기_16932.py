# https://www.acmicpc.net/problem/16932
#  https://www.acmicpc.net/problem/16946 와 유사 문제
'''
0을 1로 바꾸어서 1의 개수가 가장 많이 나오는 경우, 그 1의 합을 구하는 문제

아이디어
1. 주어진 입력에서 그룹별로 1의 개수를 카운트
2. 0의 위치를 1로 바꾸어 보면서 상하좌우 연결된 그룹의 1의 개수를 더해봄
3. 0의 위치가 연속된 그룹에 인접해 있을 수 있기 때문에 set 함수를 이용해서 처리 필요
4. 이 중에서 최대값을 답으로 선정

'''
import sys
from collections import deque,defaultdict
input = sys.stdin.readline

rr = [-1,1,0,0]
cc = [0,0,-1,1]

def matrix_print(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j],end=' ')
        print()    
    print()    

'''
# 시간 초과
def bfs(i,j):
    Q = deque()
    visited = [[0]*M for _ in range(N)]

    Q.append([i,j])
            
    cnt = 0
    while Q:
        r,c = Q.popleft()

        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]

            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and data[nr][nc]:
                    visited[nr][nc] = 1
                    Q.append((nr,nc))
                    cnt += 1
    # matrix_print(visited)
           
    return cnt


N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

result = 0
ans = 0
for i in range(N):
    for j in range(M):
        if not data[i][j]:
            # print(i,j)
            data[i][j] = 1
            ans = bfs(i,j)
            data[i][j] = 0
        result = max(result,ans)

print(result)
'''
def bfs(i,j,k):
    Q = deque()
    Q.append([i,j])
    visited[i][j] = k
    count = 1
    while Q:
        r,c = Q.popleft()
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if data[nr][nc]:
                    Q.append((nr,nc))
                    visited[nr][nc] = k
                    count += 1
    group[k] = count
    # matrix_print(visited)
    # print(group)       

N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

# 위치에 따라 그룹화 및 1의 개수 카운팅
group = defaultdict(int)
cnt = 2
for i in range(N):
    for j in range(M):
        if data[i][j] and not visited[i][j]:
            bfs(i,j,cnt)
            cnt += 1

# 상하 좌우와 인접한 그룹을 집합 gr에 넣기. 
result = 0
for i in range(N):
    for j in range(M):
        gr = set() 
        ans = 1   # 자기 자신도 카운팅해야 함.
        if not data[i][j]:
            for n in range(4):
                x = i + rr[n]
                y = j + cc[n]
                if 0 <= x < N and 0 <= y < M:
                    if visited[x][y]:
                        gr.add(visited[x][y])
            # print(gr)     
            # 그룹에 있는 1의 개수 더해주기       
            for c in gr:
                ans += group[c]            
        # 그 중 가장 최고 값이 답          
        result = max(result,ans)
print(result)
