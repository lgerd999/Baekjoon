# https://www.acmicpc.net/problem/2251
#
'''
A,B,C 물통이 있고, C물통만 가득차 있음.
어떤 물통에 들어 있는 물을 다른 물통으로 쏟아 부을 수 있는데, 한 물통이 비거나, 다른 한 물통이 가득찰 때까지 물을 부을 수 있음
(A물통의 최대 용량은 a까지 담을 수 있고, X가 담겨 있을 수 있음, B물통은 최대용량 b, Y리터가 담겨져 있을 수 있음, C도 최대용량 c, Z리터)

* 경우의 수는 총 6가지.
A -> B : B물통의 상태는 비어있꺼나 일부 물이 들어 있을 수 있음. A는 B에 A의 모든 물을 다 들이 붙거나 다 찰때까지만 들이 부을 수 있음. X,b-Y
A -> C : X, c-Z --> A물통에 있는 X 전체를 C 물통에 들이 붙거나, A물통의 c-Z 만큼만 C물통에 들어 붙거나(C물통에 Z만큼 물이 있는 경우)
B -> A : Y, a-X
B -> C : Y, c-Z
C -> A : Z, a-X
C -> B : Z, b-Y

'''
import sys
from collections import deque
input = sys.stdin.readline

def action(x,y):    
    if not visited[x][y]:
        visited[x][y] = 1
        Q.append([x,y])


def bfs():

    while Q:
        X,Y = Q.popleft()
        Z = c - X - Y   # 기본 조건에 C물통에만 물이 가득차 있고, 물을 옮기는데 따른 물의 손실은 없다라고 명시됨.
                        # 결국 A,B,C 물통 중 C물통만 꽉 차 있기 때문에 X+Y+Z=c 가 성립됨.

        if X == 0:
            result.append(Z)

        # A --> B (X - w,Y + w)
        w = min(X,b-Y)
        action(X-w,Y+w)

        # A --> C 
        w = min(X,c-Z)  # X-w, Z+w
        action(X-w,Y)   # c - X - Y + w = 

        # B --> A 
        w = min(Y,a-X)  # Y-w, X+w
        action(X+w,Y-w) # x,y좌표를 뒤집어서 입력해야 함

        # B --> C 
        w = min(Y,c-Z)  # Y-w, Z+w
        action(X,Y-w) # x,y좌표를 뒤집어서 입력해야 함, c-Z-Y = X 

        # C --> A
        w = min(Z,a-X)  # Z-w, X+w
        action(X+w,Y)   

        # C --> B 
        w = min(Z,b-Y)  # Z-w, Y+w
        action(X,Y+w)

a,b,c = map(int,input().split())
result = []
visited = [[0]*201 for _ in range(201)]
Q = deque()
Q.append([0,0])
visited[0][0] = 1

bfs()
result.sort()
print(' '.join(map(str,result)))