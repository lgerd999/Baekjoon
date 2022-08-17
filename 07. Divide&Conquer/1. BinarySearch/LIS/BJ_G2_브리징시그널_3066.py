# https://www.acmicpc.net/problem/3066
# LIS
'''
'''

import sys
from bisect import bisect_left

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    block = [int(input()) for _ in range(N)]
    # print(block)
    
    buf = [0]
    for i in block:
        if buf[-1] < i:
            buf.append(i)
        else:
            buf[bisect_left(buf,i)] = i
    print(len(buf)-1)               