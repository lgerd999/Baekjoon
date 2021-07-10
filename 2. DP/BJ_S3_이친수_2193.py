# https://www.acmicpc.net/problem/2193

N = int(input())

DP = [0]*(N+3)
DP[0] = 1
DP[1] = 1
DP[2] = 1
for i in range(3,N+1):
    DP[i] = DP[i-1] + DP[i-2]
#print(DP)    
print(DP[N])    