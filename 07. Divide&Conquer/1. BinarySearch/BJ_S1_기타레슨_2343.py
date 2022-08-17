# https://www.acmicpc.net/problem/2343
# 이분 탐색

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
data = list(map(int,input().split()))

# 하나의 강의 길이는 적어도 하나의 블루레이에는 들어가야 하므로, 
# start는 data의 가장 큰 강의 길이가 들어가고, end 는 전체 강의가 들어가는 것으로 설정
start = max(data)
end = sum(data)
result = 0
while start <= end:
    total,cnt = 0,1   # cnt가 1인 이유는 적어도 하나는 블루레이에 들어가므로.
    mid = (start + end)//2
    for i in data:        
        # 크기를 넘어가면 새로운 블루레이
        if total + i > mid:    #  total에 i가 들어가서 mid 값을 넘어버리면 total을 새로운 블루레이의 첫번째 녹화로 설정.        
            cnt += 1
            # print(i,total,mid,cnt)
            total = i
        # 아니면 같은 블루레이에 계속 녹화 
        else:
            total += i    
            
    if cnt > M:
        start = mid + 1
    # ans <= M    
    else:
        result = mid
        end = mid -1
        
print(result)            
        
