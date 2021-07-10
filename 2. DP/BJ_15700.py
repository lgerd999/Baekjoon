# B4 https://www.acmicpc.net/problem/15700

N,M = map(int,input().split())
'''
DP M=       1   2   3       4       5
N=      1   0   1   1       2       2
        2   1   2   3       4       5
        3   1   3   4       6       7
        4   2   4   6       8       10
        5   2   5   7       10      12 
          n//2  n  n//2 +n  2n 2n+ n//2

점화식 : DP[N][M] =  n//2 + (m-1)* n//2 = n//2 * m

'''    
ans = N*M //2

print(ans)
