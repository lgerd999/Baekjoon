import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
cards = list(map(int,input().split()))

buf = [0]
dp = [0]*N
for idx,i in enumerate(cards):
    if buf[-1] < i:
        buf.append(i)
        dp[idx] = len(buf) -1 
    else:
        dp[idx] = bisect_left(buf,i)
        buf[dp[idx]] = i  
print(len(buf)-1)          