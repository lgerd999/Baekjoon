#
#

import sys
input = sys.stdin.readline

data = []
N = int(input())
for _ in range(N):
    X,Y = map(int,input().split())
    data.append((X,Y))

for i in sorted(data,key = lambda x: (x[0],x[1])):
    print(*i)

    