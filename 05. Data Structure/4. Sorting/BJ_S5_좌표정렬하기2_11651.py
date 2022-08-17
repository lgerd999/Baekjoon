#
#

import sys
input = sys.stdin.readline

data = []
N = int(input())
for _ in range(N):
    data.append(list(map(int,input().split())))

for i in sorted(data,key=lambda x:(x[1],x[0])):
    # print(' '.join(i))
    print(*i)
