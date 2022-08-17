# https://www.acmicpc.net/problem/17406
#
'''

'''

import sys
input = sys.stdin.readline

def matrix_print(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j],end=' ')
        print()    

'''
회전 연산 (r,c,s)
가장 왼쪽 윗 칸 (r-s,c-s)
가장 오른쪽 아랫 칸 (r+s,c+s)
예) 회전 연산 (3,4,2) --> 5x5 matrix
가장 왼쪽 윗 칸 : (1,2)
가장 오른쪽 아랫 칸 : (5,6)

        A[r-s][c-s] [4-2+1]  [4-2+2]    [4-2+3]  [4-2+4]=[4+2] 
A[1][1]   A[1][2] → A[1][3] → A[1][4] → A[1][5] → A[1][6]
             ↑                                       ↓
A[2][1]   A[2][2]   A[2][3] → A[2][4] → A[2][5]   A[2][6]
             ↑         ↑                   ↓         ↓
A[3][1]   A[3][2]   A[3][3]   A[3][4]   A[3][5]   A[3][6]
             ↑         ↑                   ↓         ↓
A[4][1]   A[4][2]   A[4][3] ← A[4][4] ← A[4][5]   A[4][6]
             ↑                                       ↓
A[5][1]   A[5][2] ← A[5][3] ← A[5][4] ← A[5][5] ← A[5][6]

A[6][1]   A[6][2]   A[6][3]   A[6][4]   A[6][5]   A[6][6]

'''

def rotate(r,c,s):
    for i in range(2*s + 1):    # r+s - (r-s) = 2s
        for j in range(2*c + 1):



N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
rcs = [list(map(int,input().split())) for _ in range(K)]

matrix_print(arr)
matrix_print(rcs)

A = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if A[rcs[0]-rcs[2]][rcs[1]-rcs[2]] 