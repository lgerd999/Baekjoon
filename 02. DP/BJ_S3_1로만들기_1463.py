# https://www.acmicpc.net/problem/1463
N = int(input())

DP = [0]*(N+3)
DP[1:3] = [0,1,1]
for i in range(4,N+1):
    if i % 2 == 0 and i % 3 == 0:
        DP[i] = min(1+DP[i-1],1+DP[i//2],1+DP[i//3])
    elif i%2 == 0:
        DP[i] = min(1+DP[i-1],1+DP[i//2])
    elif i%3 == 0:
        DP[i] = min(1+DP[i-1],1+DP[i//3])
    else:
        DP[i] = 1+DP[i-1]    
print(DP[N])