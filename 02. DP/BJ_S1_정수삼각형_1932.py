import sys

input = sys.stdin.readline

n = int(input())
dp = [[0]*(n) for _ in range(n)]

'''
dp[0] = data[0][0]
dp[1][0] = dp[0] + data[1][0]
dp[1][1] = dp[0] + data[1][1]
dp[2][0] = dp[1][0] + data[2][0]
dp[2][1] = max(dp[1][0],dp[1][1]) + data[2][1]
dp[2][2] = dp[1][1] + data[2][2]
dp[3][0] = dp[2][0] + data[3][0]
dp[3][1] = max(dp[2][0],dp[2][1]) + data[3][1]
dp[3][2] = max(dp[2][1],dp[2][2]) + data[3][2]
dp[3][3] = dp[2][2] + data[3][3]

점화식 

'''
# data = [[-1]*n for _ in range(n)] 
data = [-1]*n

dp[0][0] = int(input())

if n >= 2:
    dp[1][0],dp[1][1] = map(int,input().split())
    dp[1][0] += dp[0][0] 
    dp[1][1] += dp[0][0]

# print(dp,data)

if n >= 3:
    for i in range(2,n):
        data = list(map(int,input().split()))
        for j in range(i+1):            
            if j == 0 or j == i+1:
                dp[i][j] = dp[i-1][j] + data[j] 
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + data[j]                    
print(max(dp[n-1]))          