import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
prog = list(map(int,input().split()))

# 이분 탐색을 이용한 방법
buf = [0]
for i in prog:
    if buf[-1] < i:
        buf.append(i)
    else:
        buf[bisect_left(buf,i)] = i
# print(buf)
print(N - (len(buf)-1))