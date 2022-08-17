# https://www.acmicpc.net/problem/3745
#

import sys
from bisect import bisect_left

input = sys.stdin.readline

while True:
    try:
        N = int(input())
        stock = map(int,input().split())
        
        buf = [0]
        for i in stock:
            if buf[-1] < i:
                buf.append(i)
            else:
                buf[bisect_left(buf,i)] = i
        print(len(buf)-1)                   
    except:
        break        
