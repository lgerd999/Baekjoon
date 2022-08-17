# https://www.acmicpc.net/problem/1818
#

import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
books = map(int,input().split())

buf =[0]
for i in books:
    if buf[-1] < i:
        buf.append(i)
    else:
        buf[bisect_left(buf,i)] = i
print(N - (len(buf)-1))                