# https://www.acmicpc.net/problem/11402
#
# 뤼카의 정리 이론 : https://bowbowbow.tistory.com/2
'''
#파스칼의 삼각형 nCk
C[n][k] = n번째 줄의 k번째 수라고 한다면,
C[n][1] = 1, C[n][n] = 1  (양쪽 끝은 1)
C[n][k] = C[n-1][k-1] + C[n-1][k]

파스칼 삼각형 방식으로 문제 해결시 발생되는 문제는 n이 매우 큰 문제(여기서는 10^18)에 대해 접근하면 메모리/시간 초과 발생함.
--> 이를 해결하기 위해 뤼카의 정리를 이용해 해결.

#Lucas(뤼카)의 정리
음이 아닌 정수 n과 k, 그리고 소수  p에 대해 다음이 성립한다.
[n ]   k    [ni]
|  | = ㅠ   |  |  (mod p) 
[m ]   i=0  [mi]
여기서, ni 와 mi 는 각각 n과 m을 p진법으로 나타낸 것이다.
 n = nk p^k + nk-1 p^k-1 + ... + n1 p + n0
 m = mk p^k + mk-1 p^k-1 + ... + m1 p + m0

예를 들어, 
[1432 ]   k    [ni]
|     | = ㅠ   |  |  (mod 7) 
[342  ]   i=0  [mi]

7진법으로 표기
1432 = 4*7^3 + 1*7^2 + 1*7^1 + 4
342  = 0*7^3 + 6*7^2 + 6*7^1 + 6

따라서 다음과 같이 나타낼 수 있다.
[1432 ]    [4] [1] [1] [4]
|     | =  | | | | | | | | (mod 7) 
[342  ]    [0] [6] [6] [6]

이때, ni < mi 이면, 
[ni]
|  | = 0 으로 취급한다.
[mi]

# x진법 str 을 10진법으로 변환
int(str,x진법)

'''
import sys
# from collections import defaultdict
input = sys.stdin.readline
N,K,M = map(int,input().split())

# 진법 변환 : n : 10진수, p : 소수이면서 변경할 진법
def conv(n,p):
    rev_base = []
    while n > 0:
        n,r = divmod(n,p)
        rev_base.append(r)        
    # print(rev_base[::-1])    
    return rev_base[::-1]

# 이항계수(binomial)
def binomial(n,k):
    C = [[0]*(n+2) for _ in range(n+2)]
    C[0][0] = 1
    for i in range(1,n+2):    
        for j in range(i):
            C[i][j] = (C[i-1][j-1] + C[i-1][j])%M
    return C[n+1][k]

# 뤼카의 정리
ans = 1
a = conv(N,M)
b = conv(K,M)

while len(a):
    x = a.pop()
    if b:
        y = b.pop()
    else:
        y = 0    
    # print(x,y)
    if x < y:
        ans = 0
        break
    ans *= binomial(x,y)
    ans %= M

print(ans)        