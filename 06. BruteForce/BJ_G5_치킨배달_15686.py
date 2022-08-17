# https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations

# 집에서 치킨집까지의 거리
def dist(x,y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

def city_dist(y):
    ssum = 0
    for i in home:
        min_d = sys.maxsize
        for j in y:
            min_d = min(min_d,dist(i,j))            
        ssum += min_d
    return ssum    
    
N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

chiken = []
home = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            chiken.append([i+1,j+1])
        elif data[i][j] == 1:
            home.append([i+1,j+1])

A = list(combinations(chiken,M))
ans = sys.maxsize
for i in A:
    ans = min(ans,city_dist(i))
print(ans)    