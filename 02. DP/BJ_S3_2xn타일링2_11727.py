# https://www.acmicpc.net/problem/11727
N = int(input())

DP = [0]*(N+1)
'''
2xn 직사각형을 2x1,1x2,2x2 타일로 채우는 방법의 수 구하기

n-1 1
    1x2
n-2 2
    1x2
    2x1
    2x2

n-1(1x2), n-2(2x2, 2x1) 총 3가지 경우의 수의 조합이므로 점화식은 아래와 같다.
점화식 : D[N] = 2* D[N-2] + D[N-1]
'''
if N >= 1:
    DP[1] = 1
if N >= 2:    
    DP[2] = 3
for i in range(3,N+1):
    DP[i] = 2*DP[i-2] + DP[i-1]
print(DP[N]%10007)    