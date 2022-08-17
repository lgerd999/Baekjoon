#https://www.acmicpc.net/problem/3020

import sys
input = sys.stdin.readline  
N,H = map(int,input().split())

# 높이가 i인 석순, H-(i-1)인 종유석
up = [0]*(H+1)
down = [0]*(H+1)

result = [0]*H

for j in range(N):
    data = int(input())
    if j %2 == 0 :   # 석순
        down[data] += 1
    else:           # 종유석
        up[H-data+1] += 1
print(down,up)
'''
# i 줄을 잘랐을 때 석순 높이가 i와 i+1 이상

1                 |
5           ||||  |  
6       ||  ||||  |
7    |  ||  ||||  | 
i    1  2    3    4  석순 길이(i) 
역순으로 누적합 계산
'''
for i in range(H-1,0,-1):    
    down[i] += down[i+1]
'''    
# i 줄을 잘랐을 때 종유석 위치가 i인 석순의 개수와 i-1이하에 위치한 종유석 개수    
i      2   3    4   종유석 길이(H-i+1) 
7     ||  |||  ||   
7     ||  |||  ||
5     ||  |||
2     ||
순서대로 계산
'''
for i in range(1,H + 1):    
    up[i] += up[i-1]
    result[i-1] = up[i]+down[i]
print(down,up,result)    
min_v = min(result)
print(min_v,result.count(min_v))    