# https://www.acmicpc.net/problem/17123

# pypy 통과
import sys
input = sys.stdin.readline

'''
(1,1)->(2,3)
3 3 3 | Row[1] = 3 * 3 = V * (C2-C1+1)
3 3 3 | Row[2] = 3 * 3 = V * (C2-C1+1)
______|
Col[1] = 3 * 2 = V * (R2-R1+1)
Col[2]
Col[3]
'''
def operator(R1,C1,R2,C2,V):
    for i in range(R1-1,R2):                  
        row[i] += V*(C2-C1+1)
    for j in range(C1-1,C2):                            
        col[j] += V*(R2-R1+1)

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(N)]
    row = [0] * N
    col = [0] * N
    # 구간 합
    for i in range(N):
        for j in range(N):
            row[i] += array[i][j]
            col[j] += array[i][j]  

    for _ in range(M):
        r1,c1,r2,c2,v = map(int,input().split())       
        operator(r1,c1,r2,c2,v)       
    
    print(*row)
    print(*col)