# https://www.acmicpc.net/problem/17122

from collections import defaultdict

table = defaultdict(int)
for i in range(8):
    table[chr(ord('A') + i)] = i
# print(table)

grid = [[0]*8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        if i%2 and j%2: # 홀수
            grid[i][j] = 1
        elif i%2 == 0 and j%2 == 0:
            grid[i][j] = 1
# print(grid)

T = int(input())
for _ in range(T):
    A, B = input().split()    
    y = int(B)//8 
    x = int(B)%8 - 1

    if x == -1:
        y -= 1
        x = 7
    #print(int(table[A[0]]),int(A[1])-1,x,y)
    if grid[x][y] == grid[ table[A[0]] ][ int(A[1])-1 ]:
        print("YES")
    else:
        print("NO")    
