# https://www.acmicpc.net/problem/2616
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
M = int(input())

# 구간 합
customer = [0]*(N+1)
for i in range(1,N+1):
    customer[i] += customer[i-1] + data[i-1]
'''
경우의 수 : 총 4가지
(1,2)->(3,4)->(5,6) or (6,7)
(1,2) or (2,3) -> (4,5) -> (6,7)

객차 N량    (1) (2)     (3)     (4)     (5)     (6)     (7)
            35  40      50      10      30      45      60 
DP[1][N]    0   35+40   40+50   90      90      90      105
DP[2][N]    0   0       0       75+60   90+40   135     165     
                                        75+60   
DP[3][N]    0   0       0       0       0       135+75  135+105

점화식 : DP[i][j] = max(DP[i][j-1], DP[i-1][j-M] + PreSum[j] - PreSum[j-M])
예) DP[2][5] = max(DP[2][4], DP[1][3] + PreSum[5] - PreSum[3])
             = max(135, 90 + 165 - 125) = 135

'''
DP = [[0]*(N+1) for _ in range(4)]
for i in range(1,4):    # 소형기관차 3대(1~3)
    for j in range(i*M,N+1): # 객차(2~7,4~7,6~7)
        DP[i][j] = max(DP[i][j-1], DP[i-1][j-M] + customer[j] - customer[j-M]) 
print(DP[3][N])