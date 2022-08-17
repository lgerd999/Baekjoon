# https://www.acmicpc.net/problem/16956
#
'''
양은 이동하지 않고 그 자리에 있고, 늑대는 인접한 칸을 자유롭게 이동.
목장에 울타리를 설치하는 문제로 울타리 개수에 대해 제한은 없다.

'''
import sys
from collections import deque
input = sys.stdin.readline

rr = [-1,1,0,0]
cc = [0,0,-1,1]

def matrix_print(A):
    print(len(A),len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j],sep='')
        # print()    

def bfs(i,j):
    Q.append((i,j))
    visited[i][j] = 1
    while Q:
        r,c = Q.popleft()     
        # print(r,c)
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]
            if 0<= nr < R and 0 <= nc < C:
                if data[nr][nc] == 'S': 
                    if data[r][c] == 'W':
                        return False          
                elif data[nr][nc] == '.':
                    visited[nr][nc] = 1
                    data[nr][nc] = 'D'
                    Q.append((nr,nc))
    return True

R,C = map(int,input().split())
data = [list(input().rstrip()) for _ in range(R)]

visited = [[0]*C for _ in range(R)]
Q = deque()
ans = False
for i in range(R):
    for j in range(C):
        if data[i][j] == 'W' :
            Q.append((i,j))

ans = bfs(i,j)
# print(ans,data,visited)

if ans:  
    print(1)
    for i in data:
        print(''.join(i))
else:
    print(0)    

