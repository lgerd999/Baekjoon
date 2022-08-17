# https://www.acmicpc.net/problem/13397
# 이분탐색
'''
N개의 수로 이루어진 1차 배열을 M개 이하의 구간으로 나누어서 구간의 점수의 최댓값을 최소로 하려고 한다.
구간은 다음 조건을 만족해야 한다.
1. 하나의 구간은 하나 이상의 연속된 수들로 이루어져 있다.(2개 이상의 수이며 연속된 구간으로 구분)
2. 배열의 각 수는 모두 하나의 구간에 포함되어  있어야 한다.

구간의 점수 = 구간에 속한 최대값 - 최소값

예) [1,5,4,6,2,1,3,7]이고 M = 3
[1,5],[4,6,2],[1,3,7]로 구간을 나누면 각 구간의 점수는 4,4,6점이 된다. 최대값은 6.
만약, [1,5,4],[6,2,1],[3,7]로 구간을 나누면, 각 구간 점수는 4,5,4이고 최대값은 5.
두 경우의 수 중 최대값이 최소인 것은 5점.

경우의 수, M = 3      구간점수  최대값
1,5 + 4,6,2,1 + 3,7 => 4,5,4 => 5
1,5 + 4,6,2 + 1,3,7 => 4,4,6 => 6
1,5 + 4,6 + 2,1,3,7 => 4,2,6 => 6
1,5,4 + 6,2,1 + 3,7 => 4,5,4 => 5
1,5,4 + 6,2 + 1,3,7 => 4,4,6 => 6
1,5,4,6 + 2,1 + 3,7 => 5,1,4 => 5
----------------------------------
최소값                           5점

'''
import sys
input = sys.stdin.readline

def section(middle):
    # 구간을 나누기 전 초기값을 배열의 첫번재값으로 설정
    max_s = arr[0]
    min_s = arr[0]
    cnt = 1 #
    for i in range(1,N):
        # 구간에서 배열 값이 최대값보다 크면 최대값을 다시 설정
        if arr[i] > max_s:
            max_s = arr[i]
        # 구간에서 배열 값이 최소값보다 작으면 최소값을 다시 설정
        elif arr[i] < min_s:
            min_s = arr[i]
        # 구간 점수가 이분탐색의 기준값(mid)보다 크면, 구간 생성
        if max_s - min_s > middle:
            cnt += 1
            # 구간이 결정되면 다음 구간을 위한 초기값 설정
            max_s = arr[i]
            min_s = arr[i]
        # print(max_s,min_s,cnt)
    return cnt        

N,M = map(int,input().split())  
arr = list(map(int,input().split()))

start = 0
end = max(arr)
ans = 0
while start <= end:
    mid = (start + end)//2
    # 구간이 M 보다 같거나 작으면,
    if section(mid) <= M:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1        
print(ans)        

