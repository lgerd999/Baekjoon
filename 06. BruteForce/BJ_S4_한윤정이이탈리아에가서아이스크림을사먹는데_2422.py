# https://www.acmicpc.net/problem/2422
#
'''
N = 아이스크림 종류의 수, M = 섞어먹으면 안되는 조합의 개수
아이스크림을 3가지 선택.
3가지 중 섞으면 안되는 조합의 자리수 => (0,1),(1,2),(0,2)

구현
1. 섞지 말아야 할 조합 첫 번재가 x,y  라면,
not_mix[0][1],not_mix[1][2],not_mix[0][2] 자리에 해당 조합이 포함되지 않으면 된다.

'''
import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
result = set()
   
check = [[False] * (N+1)  for _ in range(N+1)]
for i in range(M):
    x,y = map(int,input().split())
    check[x][y] = True
    check[y][x] = True

for c in combinations(range(1,N+1),3):               
    if check[c[0]][c[1]] or check[c[1]][c[2]] or check[c[0]][c[2]]:        
        continue        
    result.add(c)

print(len(result))            
            
'''
4 1
1 4
---- 
(1,2,3),(2,3,4)
2
'''    

