# https://www.acmicpc.net/problem/2839

N = int(input())
DP = [-1] * 5001
DP[3] = 1
DP[5] = 1

for i in range(6,N+1):    
    if (i % 3)%5 == 0 and (i % 5)%3 == 0:
        DP[i] = min(DP[3] + DP[i-3],DP[5] + DP[i-5])        
    elif DP[i - 5] != -1 or i%5 == 0:        
        DP[i] = DP[5] + DP[i-5]        
    elif DP[i - 3] != -1 or i%3 == 0:        
        DP[i] = DP[3] + DP[i-3]     
     
print(DP[N])    