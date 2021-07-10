# https://www.acmicpc.net/problem/2805
#from bisect import bisect_left
from collections import Counter
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
H = list(map(int,input().split()))
   
ans = 0
tree = Counter(H)
left,right = 0,max(H)    
while left <= right:
    mid = left + (right-left)//2
    cnt = 0
    for key,value in tree.items():
        if key > mid:
            cnt += (key-mid)*value
        
    if cnt < M:
        right = mid -1
    else:
        ans = mid
        left = mid +1        
print(ans)    

