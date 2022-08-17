# https://www.acmicpc.net/problem/2470
# 투포인트 방식

import sys
input = sys.stdin.readline

N = int(input())
liq = list(map(int,input().split()))
liq = sorted(liq)

start = 0
end = N-1
left,right = 0,0
target = liq[start] + liq[end]
# start와 end가 같으면 안됨.
while start < end:
    mix = liq[start] + liq[end]
    # 특성값이 최소값을 갖는다면
    if abs(mix) <= abs(target):
        left,right = start,end
        target = mix
    # 특성값이 0보다 작으면 start를 증가시켜 0에 가깝게 한다.    
    if mix < 0:
        start += 1
    else:
        end -= 1  
print(liq[left],liq[right])