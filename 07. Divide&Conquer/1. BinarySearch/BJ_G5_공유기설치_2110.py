# https://www.acmicpc.net/problem/2110
# 이분 탐색 - 최소에서 최대를 구하는 문제 또는 최대에서 최소를 구하는 문제 유형.

'''
집이 N개가 있고, C개의 공유기를 설치할려고 하는데, 인접한 공유기 사이의 거리가 최대가 되도록 하려 할때 그때의 최대 거리를 구하는 문제

아이디어
1. 거리가 1일때 부터 거리를 늘려가는 방법. 공유기 숫자가 C개를 훨씬 상회하게 됨.
2. 거리가 늘어감에 따라 공유기 숫자가 C개에 수렴하게 됨.
3. 이때 공유기 숫자 C 개일때 거리를 구하면 됨.
'''

import sys
input = sys.stdin.readline

N,C = map(int,input().split())
home = sorted(list(int(input().rstrip()) for _ in range(N)))

# 시작은 최소거리, 끝은 최대 거리로 설정
start = 1
end = home[N-1] - home[0]
result = 0

while start <= end:    
    mid = (start + end)//2         
    last = home[0]  # 현 위치 
    cnt = 1
    for x in range(1,N):
        # 인접 위치에서 현재 위치까지의 거리가 mid 보다 크거나 같다면, 공유기 설치 가능하므로 cnt 증가
        if home[x] - last >= mid:       
            cnt += 1
            last = home[x]  # 현 위치 업데이트
            
    # cnt 수가 공유기 설치개수 C보다 작다면 end 위치를 mid -1 감소(왼쪽으로 탐색)        
    if cnt < C :
       end = mid - 1       
    else:
        result = mid
        start = mid + 1       
print(result)        