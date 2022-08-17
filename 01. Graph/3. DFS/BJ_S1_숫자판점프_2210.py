#
#
'''
5x5 숫자판에서 임의의 위치에서 시작해서 인접해 있는 네 방향으로 다섯번 이동하면서, 각 칸에 적혀 있는 숫자를 차례로 붙이면 6자리의 수
가 만들어 진다.

조건1. 이동할 때 한번 거쳤던 칸을 다시 거쳐도 됨.
조건2. 0으로 시작하는 000123과 같은 수로 만들 수 있음.

서로 다른 여섯 자리 수들의 개수를 구하는 문제

'''
import sys
input = sys.stdin.readline
rr = [-1,1,0,0]
cc = [0,0,-1,1]

def dfs(r,c,num):    
    if len(num) == 6:
        # if num not in path:
        path.add(num)
        return 
    
    for n in range(4):
        nr = r + rr[n]
        nc = c + cc[n]
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr,nc,num+board[nr][nc])

# 5 x 5 크기의 숫자판 입력
board = [list(input().rstrip().split()) for _ in range(5)]    

path = set()
for i in range(5):
    for j in range(5):
        dfs(i,j,board[i][j])
# print(path)
print(len(path))

