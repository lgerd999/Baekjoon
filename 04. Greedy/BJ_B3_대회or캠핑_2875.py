# https://www.acmicpc.net/problem/2875
#
'''
N : 여학생 수
M : 남학생 수
K : 인턴쉽 프로그램 참여자 수
대회에 나가려면 여학생 2명, 남학생 1명이 한팀으로 결성되어야 하고 인턴쉽에 참여자는 대회에 나갈 수 없다.

예로, N = 6, M = 3, K = 2라면
3팀이 나갈 수 있는데, 인턴쉽이 2명이 포함되어야 하므로 1명씩 빼면 총 2팀이 나갈 수 있다.

구현
1. M - N//2 가 최초 팀 수
2. N%2, M-N//2 에서 각각 K 수만큼 차출하고 부족하면 팀(3)수에서 하나씩 뺀다.

'''
import sys
intput = sys.stdin.readline

N,M,K = map(int,input().split())

# 대회 나갈 팀 수 구하기
# N = 6, M = 3, Team = 3
# M - N//2가 0 이면 team = M, M - N//2 > 0, team = N//2, M- N//2 < 0, team = M
team = M - N//2
if team <= 0:
    team = M
    remain = N - M * 2
else:
    team = N//2
    remain = N%2 + M-N//2
# print(team,remain)

# 인턴쉽 참여자 수
# 부족 인원 수 3이하이면 1개 줄이고 6이하면 2개 줄이고
while remain < K and team > 0:
    team -= 1
    remain += 3

print(team)