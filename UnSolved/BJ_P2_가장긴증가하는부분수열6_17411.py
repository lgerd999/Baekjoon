# https://www.acmicpc.net/problem/17411
#
'''

'''
import sys
from bisect import bisect_left
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
prog = list(map(int,input().split()))

buf = [-INF]
dp = [0]*(N+1)
cnt = 0
for idx,i in enumerate(prog):
    if buf[-1] < i:
        buf.append(i)
        dp[idx] = len(buf) -1
    else:
        dp[idx] = bisect_left(buf,i)
        buf[dp[idx]] = i            
        print(buf,dp)
print(len(buf)-1)
#print(buf,dp)

# 가장 큰 값부터 거슬러 올라가며 부분 수열을 찾는다.
result = []
value = max(dp)+1
for i in range(N-1,-1,-1): # dp[N-1] ~ dp[0]
    if dp[i] == value-1:    # 가장 긴 증가하는 부분수열 길이가 최대. value = value -1 
        result.append(prog[i])  # 그 때 prog[i]에 있는 값 추가 
        value = dp[i]       # 제일 먼저 값이 같아지는 index 
        
'''
10    <-- N
-61 -28 -72 59 13 -21 84 -76 -52 -1  <-- prog
4
[-9223372036854775807, -76, -52, -21, -1] [1, 2, 1, 3, 3, 3, 4, 1, 2, 4, 0]  <-- buf, dp
-61 -28 -21 -1      <- result
'''     
print(' '.join(map(str,result[::-1])))
