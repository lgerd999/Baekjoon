# https://www.acmicpc.net/problem/2749
# https://www.acmicpc.net/problem/11444
from itertools import product
import sys
from collections import defaultdict,deque
'''
피노나치 점화식을 행렬로 나타내고 이를 거듭제곱(분할 정복)을 이용해서 풀면 시간초과도 벗어날 수 있음.

[Fn+2]   [1 1][Fn-1]
|    | = |   ||    |
[Fn+1]   [1 0][Fn  ]

아래 식으로 변형

[Fn+1 Fn  ]   [1 1]^n
|         | = |   |
[Fn   Fn-1]   [1 0]

'''

input = sys.stdin.readline

N = int(input())

'''
# 기존 방식으로 하면 메모리 초과 발생
dp = defaultdict(int)
dp[0],dp[1] = 1,1
for i in range(2,N):
    dp[i] = (dp[i-1]+dp[i-2])%1000000

print(dp[N-1])
'''
'''
# deque 방식으로 변경하였으나 시간초과 발생
dp = deque()
dp.append(1)
dp.append(1)

index = 2
while True:
    if index == N:
        break
    dp.append((dp[0]+dp[1])%1000000)
    x = dp.popleft()
    index += 1 
print(dp[-1])
'''
def product_mul(A,B):
    len_A = len(A)
    ans = [[0]*len_A for _ in range(len_A)]
    for  i in range(len_A):
        for j in range(len_A):
            s = 0
            for k in range(len_A):
                s += A[i][k] * B[k][j]
            ans[i][j] = s % 1000000
    return ans

# 분할정복
def matrix_squar(A,n):
    len_A = len(A)
    if n == 1:
        for i in range(len_A):
            for j in range(len_A):
                A[i][j] %= 1000000
        return A
    mul = matrix_squar(A,n//2)        
    if n % 2 :
        return product_mul(product_mul(mul,mul),A)
    else:
        return product_mul(mul,mul)

print(matrix_squar([[1,1],[1,0]],N)[1][0])