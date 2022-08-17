# https://www.acmicpc.net/problem/1904

N = int(input())
'''
n = 1, 1
n = 2, 00 11
n = 3, 001 100 111
n = 4, 0000 0011 1100 1111 1001
n = 5, 00001 00111 11001 10011 11111 11100

| n-2 | 00 와 | n-1 | 1
점화식 DP[N] = DP[N-2] + DP[N-1]
'''
DP = [0]*(N+1)
DP[1:2] = [1,2]
for i in range(3,N+1):
    DP[i] = (DP[i-2] + DP[i-1])%15746
print(DP[N])    
