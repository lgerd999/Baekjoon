# https://www.acmicpc.net/problem/1018

import sys
def window(grid,i,j,wb):
    cnt = 0
    for n in range(8):
        for m in range(8):  
            # 기준이 되는 색상 wb 위치가 n,m 좌표상 짝수행/짝수열에 위치하거나 홀수행/홀수열에 위치함      
            if (n%2 == 0 and m%2 == 0) or (n%2==1 and m%2==1):
                if grid[i+n][j+m] != wb:       # 기준 색상이 와야 할 자리에 다른 색상이 온 경우에 대해 카운트
                    cnt += 1
            else:        
                if grid[i+n][j+m] == wb:       # 다른 색상이 와야 할 자리에 기준 색상이 온 경우에 대해 카운트 
                    cnt += 1
    return cnt            

N,M = map(int,input().split())
data = [list(map(str,input().rstrip())) for _ in range(N)]
#print(data)

ans = sys.maxsize
for i in range(N-7):
    for j in range(M-7): 
        # 다시 칠해야 하는 8x8 정사각형 개수를 최소로 하기 위해서 기준이 되는 첫 시작 색에 대해 W와 B 모두 고려해 주어야 함(반례로 기준 색상만 수정하면 최소로 되는 경우 있음)
        color = 'W'
        ans = min(ans,window(data,i,j,color))     
        color = 'B'
        ans = min(ans,window(data,i,j,color))          
print(ans)
