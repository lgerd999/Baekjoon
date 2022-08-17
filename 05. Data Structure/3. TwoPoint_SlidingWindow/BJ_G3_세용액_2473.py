# https://www.acmicpc.net/problem/2473
#
'''
용액 하나를 정해 놓고 그 위치가 i라고 한다면, 나머지 2개의 용액은 i+1 ~ N-1까지 투 포인터로 최소값을 계산할 수 있다. 

'''

import sys
input = sys.stdin.readline

N = int(input())
liq = list(map(int,input().split()))
liq = sorted(liq)
# print(liq)

target = sys.maxsize
# start를 지정하고 left와 right를 투 포인터로 구현
for start in range(N-2):
    left,right = start+1,N-1
    while left < right :
        mix = liq[start] + liq[left] + liq[right]
        if abs(mix) <  target:
            l1,l2,l3 = start,left,right
            target = abs(mix)
        # 혼합액의 특성값이 0에 가까워지기 위해 left값을 증가    
        if mix < 0:
            left += 1
        # 특성값이 0을 넘엇ㅆ다면 right 값을 증가    
        elif mix > 0:
            right -= 1
        # 특성값이 0이라면 중지.    
        else:
            break             
print(liq[l1],liq[l2],liq[l3])