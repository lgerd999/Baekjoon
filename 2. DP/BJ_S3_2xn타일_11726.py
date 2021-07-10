# https://www.acmicpc.net/problem/11726
N = int(input())

DP = [0]*(N+1)
'''
2xn 타일에서 1x2,2x1 타일로 채우는 방법의 수 구하기
n-1  1가지
    2x1
n-2  2가지
    2x1 2개
    1x2 2개    
n-3 은 n-1 에 포함
n-4 는 n-2 에 포함
...

점화식 : DP[N] = DP[N-2] + DP[N-1]
'''
if N <= 2: 
    DP[N] = N
else:    
    DP[1] = 1
    DP[2] = 2
    for i in range(3,N+1):
        DP[i] = DP[i-2] + DP[i-1]
print(DP[N]%10007)    