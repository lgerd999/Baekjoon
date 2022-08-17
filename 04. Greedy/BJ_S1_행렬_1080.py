# https://www.acmicpc.net/problem/1080
# 

'''
아이디어 : A행렬의 (i,j)과 B행렬의 (i,j)의 값을 비교하여 값이 다르면 3X3 을 뒤집는다.

'''

import sys
input = sys.stdin.readline

def mirror(matrix,x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            if matrix[i][j] == '0':
                matrix[i][j] = '1'
            else:
                matrix[i][j] = '0'    
    return matrix            

N,M = map(int,input().split())
A = [list(input().rstrip()) for _ in range(N)]
B = [list(input().rstrip()) for _ in range(N)]

cnt = 0
for i in range(N-3+1):
    for j in range(M-3+1):
        if A[i][j] != B[i][j]:
            A = mirror(A,i,j)
            cnt += 1

if A == B:
    print(cnt)            
else:
    print(-1)    
        