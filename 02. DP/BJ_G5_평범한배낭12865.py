# 평범한 배낭 : https://www.acmicpc.net/problem/12865
# 참조 : https://fbtmdwhd33.tistory.com/60

def matrix_print(grid):
    for i in range(len(grid)):
        for j in grid[i]:
            print(j, end=' ')
        print()    

# N,K = map(int,input().split())
# P = [list(map(int,input().split())) for _ in range(N)]
# print(P)

N,K = 4,7
P  = [[6, 13], [4, 8], [3, 6], [5, 12]]
'''
N,K
(W,V) x N
여행에 필요한 N개의 물건은 각각 무게 W와 가치 V를 가지고 있으며 배낭에 넣어서 가면 V만큼 즐길 수 있음
최대 K만큼의 무게를 넣을 수 있는 배낭에 넣을 수 있는 물건 값들의 최대값 구하기

DP[N][K]=  0 1 2    3          4        5                                   6                                        7
i=0        0 0 0    0          0        0                                   0                                        0 
i=1        0 0 0    0          0        0                                  13                           max(DP[0][7-6]+13,DP[0][7])=13 (6,13)
i=2        0 0 0    0          8     max(DP[1][5-4]+8,DP[1][5])=8     max(DP[1][6-4]+ 8,DP[1][6])=13    max(DP[1][7-4]+ 8,DP[1][7])=13 (4,8) 
i=3        0 0 0    6      DP[2][4]  max(DP[2][5-3]+6,DP[2][5])=8     max(DP[2][6-3]+ 6,DP[2][6])=13    max(DP[2][7-3]+ 6,DP[2][7])=14 (3,6)
i=4        0 0 0 DP[3][3]  DP[3][4]    12                             max(DP[3][6-5]+12,DP[3][6])=13    max(DP[3][7-5]+12,DP[3][7])=14 (5,12)
                   
점화식 : DP[N][K] = max(DP[N-1][K-P[N][0]] + P[N][1], DP[N-1][K])
        
'''
dp = [[0] * (K+1) for _ in range(N+1)]  # dp[data item][weight K]

for i, x in enumerate(P,1):
    for w in range(1,K+1):    
        if w < x[0]:   # 현 무게 대비 현 데이터가 더 크면 이전 dp값과 동일
            dp[i][w] = dp[i-1][w]
        elif x[0]== w:
            dp[i][w] = x[1]
        else:            # 현 무게에서 현 데이터 값을 뺀 dp 값 위치에 가중치를 더 한 값과 이전 무게의 dp값 중 최대값
            dp[i][w] = max(dp[i-1][w-x[0]] + x[1],dp[i-1][w]) # dp[이전 물건 개수][최대무게-담을 물건의 무게] + 담을 물건의 가치]
print(dp[N][K])
    

