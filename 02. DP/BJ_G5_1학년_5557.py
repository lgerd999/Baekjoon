# https://www.acmicpc.net/problem/5557
# 참조 : https://rhdtka21.tistory.com/81

def matrix_print(data):
    for i in range(len(data)):
        for j in data[i]:
            print(j,end='   ')
        print()    

N = int(input())
data = list(map(int,input().split()))
DP = [[0]* 21 for _ in range(N+1)]
'''
입력     8       3         2        4       8 7 2 4 0 8 8
DP    [1][8]  [2][5]    [3][3]-  [4][7]+                        
              [2][11]   [3][7]+  [4][3]-  
                        [3][9]-  [4][11]+     .....
                        [3][13]+ [4][5]-
                                 [4][13]+
                                 [4][9]-
                                 [4][17]+

- 왼쪽 8부터 계산할 때 중간 계산되는 수가 모두 0~20 사이의 값이어야 함.

점화식 : DP[다음 index][ +- 가능한 모든 조합] += DP[index][조합]

* 초기값
DP[0+1][0+8] = 1(경우의 수)

* for문을 돌 다 DP[1][8]의 값이 1(DP[i][j] > 0)이기 때문에 경우의 수 계산 진행 . 이때 i=1,j=8,data[i] = 3임
DP[1+1][8-3] = DP[2][5]  + DP[1][8] = 0 + 1
DP[1+1][8+3] = DP[2][11] + DP[1][8] = 1   

* for문을 돌 다 DP[2][5]와 DP[2][11]의 값이 1(DP[i][j] > 0)이기 때문에 경우의 수 계산 진행 . 이때 i=2,j=5,11,data[i] = 2임
DP[2+1][5-2] = DP[3][3] + DP[2][5]
DP[2+1][5+2]
DP[2+1][11-2]
DP[2+1][11+2]


'''
DP[1][data[0]] = 1
for i in range(1,N):
    for j in range(21):
        if DP[i][j] > 0:    # 앞서 계산했던 DP[i+1]의 값이 있을 때
            if 0 <= j+data[i] <= 20:    # + 경우의 수 구함
                DP[i+1][j+data[i]] += DP[i][j]
            if 0 <= j-data[i] <= 20:    # - 경우의 수 구함
                DP[i+1][j-data[i]] += DP[i][j]       
matrix_print(DP)
print(DP[N-1][data[N-1]])        # DP[마지막 index - 1][수열의 합]