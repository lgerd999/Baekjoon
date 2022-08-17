# https://www.acmicpc.net/problem/1629
# 분할 정복
'''
A,B,C가 주어졌을 때, 주어지는 값들이 2,147,483,647 이하 자연수라는 조건이 있음.
(dp로 풀 경우, 값이 커질 수록 시간 초과 발생확률이 높아짐)
==> 곱셈의 크기가 커질 수록 시간 초과 발생확률이 높아짐에 따라 적절히 분할 정복 기법으로 분산해서 계산해야 함.
==> 곱셈의 크기가 커지지 않도록 적절히 C로 나누어야 함.
    이때 사용할 수 있는 수학 이론은 나머지 분배 법칙을 사용할 수 있다.
    (AxB)%C = (A%C * B%C) %C

'''
import sys
input = sys.stdin.readline

def multiply(X,Y):
    # B가 1이면 A%C를 리턴.
    if Y == 1:
        return X % C
    else:
        # 분할 정복
        # A^(B/2)
        ans = multiply(X,Y//2)  # B = B의 1/2  X  1/2
        if Y %2:    # 나머지가 홀수
            return ans * ans * X % C    # B가 11이면, B^5 X B^5 X B
        else:   # 나머지가 짝수
            return ans * ans %C         # B가 10이면, B^5 X B^5
      
A,B,C = map(int,input().split())
print(multiply(A,B))


'''
# 이진수를 이용한 계산을 분리하여 구현(시간 초과)
D = bin(B)[2:]
Q = defaultdict(int)
for i in range(len(D),0,-1): # 이진수를 역순으로 해야 계산하기 편함
    if D[len(D)-i] == '1':
        Q[len(D)-i] = i-1

S = []
for i in range(Q[0]+1):
    S.append(pow(A,2**i)%C)

ans = 1
for i in range(len(Q)):
    ans *= S[Q[i]] %C
print(ans%C)
'''

'''
# dp 구현(시간초과)
dp = defaultdict(lambda:1)
dp[1] = A
# dp[2] = A * A
for i in range(2,B+1):
    d = int(math.log2(i))
    if i == pow(2,d):
        dp[i] = dp[i//2] * dp[i//2]
    else:    
        dp[i] = dp[pow(2,d)] * dp[i-pow(2,d)]
    # print(i,d,pow(2,d),i-pow(2,d))
    
print(dp[B]%C)    
'''