# https://www.acmicpc.net/problem/11000
# https://blog.naver.com/thomaswook/222295383887

import sys,heapq
from collections import deque
input = sys.stdin.readline
N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
# print(data)
# N = 3
# data = [[1, 3], [2, 4], [3, 5]] # 2
# N = 4
# data = [[1, 1], [2, 2], [2, 3], [3, 4]] # 1

data.sort(key=lambda x:(x[0],x[1])) # 시작 시간으로 정렬, 회의실 문제와는 조금 다름
last = [data[0][1]] # 첫 시작 강의 종료 시간을 기준
cnt = 1 # 강의실은 무조건 1개 이상
for i in range(1,N):
    if data[i][0] >= last[0]:   # 매 강의 시작 시간과 마지막 강의 종료 시간 비교해서 시작 시간이 같거나 큰경우 수업은 이어서 진행하므로 연장된 시간으로 업데이트
        heapq.heappop(last)
        heapq.heappush(last,data[i][1])
    else:         # 그 외에는 강의실 추가 
        heapq.heappush(last,data[i][1])
        cnt += 1
print(cnt)     