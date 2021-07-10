# https://www.acmicpc.net/problem/14501
# 참조 : https://yabmoons.tistory.com/519

import sys
readline = sys.stdin.readline
N = int(readline())
data = [list(map(int,readline().split())) for _ in range(N)]
# print(data)
# N = 7
# data = [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]
'''
오늘부터 N+1일째 되는 날에 퇴사하는데, 남은 N일 동안 최대한 많은 상담.
           1  2  3  4  5  6   7
Ti(기간)   3  5  1  1  2  4   2
Pi(금액)  10 20 10 20 15 40 200

 - N=6,7일째 날에는 상담기간이 퇴사 후에 진행되기 때문에 진행 불가
 - 퇴사일 기준 역순으로 계산(N=7이면, 퇴사 날짜는 8일 다음날이기때문에 8일째까지는 일을 한다.)
N   7       6             5                  4                    3              2                 1
Ti  0       0             2                  1                    1              5                 3
Pi  200    40            15                 20                   10             20                10
DP  0   DP[7]     DP[5+T[5]]+15       DP[4+T[4]]+20       DP[3+T[3]]+10      DP[3]              DP[2]
일안했을때               DP[6]               DP[5]               DP[4]                             

점화식 DP[N] = max(DP[N+1],DP[N+T[N]] + P[N]), if N+1 < i + T[N] : DP[N] = DP[N+1]
-> 일을 했을때와 안했을 때 중 최대값을 선택

'''
DP = [0] * (N+5)
# 순서대로 푸는 방법
# for i in range(N+1):
#     for j in range(i):
#         DP[i] = max(DP[i],DP[j])  # 현재 날짜까지 모든 경우의 수 중 가장 최대 값 선택
#         if i == j+data[j][0]: # 현재 날과 앞으로 일할 날을 합친 값이 i와 값을 때
#             DP[i] = max(DP[i], DP[j] + data[j][1])
#         print(DP)            
# print(max(DP))        

# 역순으로 푸는 방법
ans = 0
for i in range(N,0,-1):    
    if (i+data[i-1][0]) > (N+1): # 퇴사 날짜를 넘어가는 경우
        DP[i] = DP[i+1]
    else :                       # 역순까지의 DP값과 현재 DP값 중 최대값을 선택
        DP[i] = max(DP[i+1],DP[i+data[i-1][0]] + data[i-1][1])                
        print(DP)
    if ans < DP[i]:
        ans = DP[i]            
print(ans)