
# https://www.acmicpc.net/problem/2133

N = int(input())
DP = [0]*(N+1)
'''
3xN 크기의 벽을 2x1(B), 1x2(A) 크기의 타일로 채우는 경우의 수 구하기

n-1 1(3x1)
    존재하지 않음(1x2를 삽입시 아래 빈공간 하나가 남음)
n-2 2(3x2)
    1x2, 1x2 & 2x1, 2x1 & 1x2 조합 : 3가지 경우
n-3 3(3x3)    
    존재하지 않음(빈공간 발생)
n-4 4(3x4)  
    아래와 같이 2가지 경우들이 추가됨      
    ________________    ________________
    |   |______|   |    |_______________|
    |___|______|___|    |   |_______|   |
    |_______|______|    |___|_______|___|

점화식 : DP[N] = 3* DP[N-2] + 2* DP[N-4] + 2* DP[N-6]+ .... + 2* DP[0]

'''
DP[0] = 1
for i in range(2,N+1):
    DP[i] = 3* DP[i-2]
    for j in range(4,i+1,2):        
        DP[i] += 2*DP[i-j]
print(DP[N])