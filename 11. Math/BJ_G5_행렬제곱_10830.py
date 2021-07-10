# https://www.acmicpc.net/problem/10830
import copy
# 행렬의 곱 연산
def matrix_product(A,B):
    C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] = (C[i][j] + A[i][k]*B[k][j])%1000
    return C

N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]         

# 단위 행렬   
E = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i==j:
            E[i][j] = 1

D = bin(M)[2:]
Q =[]
for i in range(len(D),0,-1):
    if D[len(D)-i] == '0':
        Q.append(-1)    # 0 인 경우 한번 더 계산해 주어야 하므로 계산이 필요없을 경우는 -1로 정의함
    else:    
        Q.append(i-1)
print('Q=',Q,len(Q))

# Q 의 첫번째 인덱스에 있는 값만 계산하면 나머지 인덱스 위치에서의 계산은 필요치 않도록 S에 계산값을 저장
S =[]
ans = copy.deepcopy(data)
for i in range(Q[0]):
    ans = matrix_product(ans,ans)   
    S.append(ans)
S.reverse()  # Q 인덱스 위치와 맞추기 위해 reserve함

# del을 이용해 삭제하는 경우 기존 위치한 index와 달라지기 때문에 계산을 다시 해야 함 
# Q의 index 위치에 있는 값이 -1인 경우 계산이 불필요하기 때문에 S index 위치에 있는 값도 삭제함
cnt =0
for i in range(len(S)):
    if Q[i] == -1:                
        del S[i-cnt]
        cnt += 1

# M = 1인 경우 S[0]가 null이 되므로 이때는 단위 행렬을 곱하여 표현
if S:
    sol = S[0]
    for i in range(1,len(S)):
        sol = matrix_product(sol,S[i])
else:
    sol = E

# Q의 마지막 index값이 0인 경우는 거듭 제곱 형태가 아니므로 아래와 같이 계산함
if Q[-1] == 0:
    sol = matrix_product(sol,data)

for i in range(len(sol)):
    print(*sol[i])
