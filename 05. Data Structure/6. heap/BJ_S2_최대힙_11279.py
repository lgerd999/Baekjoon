# https://www.acmicpc.net/problem/11279

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
Q = []
for _ in range(N):
    x = int(input())
    if x :
        heappush(Q,-x)
    else:
        if Q:
            print(-heappop(Q))        
        else:
            print(0) 