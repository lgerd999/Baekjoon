# https://www.acmicpc.net/problem/11658
# 
'''
2차원 Fenwick Tree


 (1,1)             y1(b)  y2(d)
     ---------------------
     | S[x1-1][y1-1] |    |
     | (두번 빠짐)    |  ==|> S[x1-1][y2]
     |               |    |
x1(a)|---------------|----|(x1-1,y2)
     | S[x2][y1-1]   |  ==|> S[x2][y2]
x2(c) --------------------- (x2,y2)
                  (x2,y1-1)
                  
S[x2][y2] - S[x2][y1-1] - S[x1-1][y2] + S[x1-1][y1-1] = A[x2][y2]

'''
import sys
input = sys.stdin.readline

def query(x,y):
    ans = 0 
    while x > 0:
        dy = y        
        while dy > 0:
            ans += tree[x][dy]
            dy -= (dy&-dy)
        x -= (x & -x)
    return ans

def update(x,y,val):
    while x <= N:
        dy = y
        while dy <= N:
            tree[x][dy] += val
            dy += (dy&-dy)
        x += (x & -x)
    

# N : 표의 크기, M : 합을 구해야 하는 횟수
N,M = map(int,input().split())        
S = [list(map(int,input().split())) for _ in range(N)]

tree = [[0]*1025 for _ in range(1025)]

for i in range(1,N+1):
    for j in range(1,N+1):
        update(i,j,S[i-1][j-1])
        
# print(tree)        

ans = 0
for _ in range(1,M+1):
    op = list(map(int,input().split()))
    # (x,y) -> c로 바꾸는 연산
    if op[0] == 0:        
        # op[1] = x, op[2] = y
        update(op[1],op[2],op[3]-S[op[1]-1][op[2]-1])
        S[op[1]-1][op[2]-1] = op[3]
    else:      # (x1,y1) 부터 (x2,y2)까지의 합 출력        
        #  op[1]=x1, op[2]=y1, op[3]=x2, op[4]=y2
        #    S[x2][y2]               -S[x2][y1-1]         -S[x1-1]][y2]           +S[x1][y1]
        ans = query(op[3],op[4]) - query(op[3],op[2]-1) - query(op[1]-1,op[4]) + query(op[1]-1,op[2]-1)
        print(ans)
        