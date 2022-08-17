'''
dp[0] ~ dp[5] : dp[i] = dp[i-1] +1 
dp[6] = dp[3]*2(ACV)
dp[7] = 3A(3) + ACV(3) + V = 9 (3배)
  --> dp[7] = dp[3](3A)*3(ACV+V) = 9
            = dp[4](4A)*2(ACV) = 8 
dp[8] = dp[3]*4(ACV+2V) = 12
      = dp[4]*3(ACV+V) = 12
      = dp[5]*2(ACV) = 10 
dp[9] = dp[3]*5(ACV+3V) = 15
      = dp[4]*4(ACV+2V) = 16
      = dp[5]*3(ACV+V) = 15
      = dp[6]*2(ACV) = 12
dp[10] = dp[3]*6(ACV+V+ACV)= dp[7]*2(ACV) = 18 
       = dp[4]*5(ACV+3V) = 20       
       = dp[5]*4(ACV+2V) = 20
       = dp[6]*3(ACV+V) = 18
       = dp[7]*2(ACV)= 18
 --> dp[4] ~ dp[7] : 4개만 보면 됨.      
dp[11] = dp[3]*3(ACV+V+ACV+V) = dp[7]*3(ACV+V) = 27
       = dp[4]*6(ACV+V+ACV) = dp[8]*2(ACV) = 24
       = dp[5]*5(ACV+3V) = 25
       = dp[6]*4(ACV+2V) = 24
 --> dp[5] ~ dp[8] : 4개만 보면 됨.            
...
========= 정리 ============
점화식 : 

dp[i] = dp[i-j)]*(j-1), j= 3~i
 
'''

N = int(input())

dp = [0] * (N)
dp[0] = 1
for i in range(1,N):
    dp[i] = dp[i-1] + 1

    if i > 5:
        for j in range(3,i):
            dp[i] = max(dp[i],dp[i-j]*(j-1))  
print(dp[N-1])      