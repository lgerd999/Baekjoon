# https://www.acmicpc.net/problem/1756
import sys
from bisect import bisect_left,bisect_right
input = sys.stdin.readline

D,N = map(int,input().split())
oven = list(map(int,input().split()))
P = list(map(int,input().split()))

for i in range(1,D):
    if oven[i] > oven[i-1]:
        oven[i] = oven[i-1]
oven.reverse()
#print(oven)
idx = -1
for i in P:    
    idx = bisect_left(oven,i,idx+1)
    #print(i,idx)
#    if idx == -1:
#        break
if D-idx < 0:        
    print(0)
else:     
    print(D-idx)    
  