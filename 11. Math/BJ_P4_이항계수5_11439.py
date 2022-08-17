# https://www.acmicpc.net/problem/11439
# 참고 : https://nicotina04.tistory.com/57
# https://www.acmicpc.net/problem/2004 참고
'''
이항계수4 번 문제와 차이점은 M값이 어마무시하게 크다. 그리고, 소수라는 명시도 없어졌다.
그러므로 지금까지 알고 있는 뤼케(나누는 수가 소수만 가능), 페르마(두 수가 서로소가 아닌 경우가 있어 불가) 모두 사용할 수 없다.

1. 소인수 분해
- 정의 : 자연수를 소인수들의 곱으로 표현. 
예를 들어, 60을 소인수 분해하면, 60을 2(소수)로 나누면 몫이 30. 이를 다시 소수 2로 나누면 15. 15는 2로 나눌 수 없으므로 그 다음 소수인 3으로 나눔
그러면 몫은 5가 남는데 5는 소수이므로 소인수 분해 종료. 결국 60 = 2 x 2 x 3 x 5 = 2^2 x 3 x 5

N 이하의 소수를 에라토스테네스의 체 알고리즘을 이용하여 구함.
그리고, 해당 소수가 이항계수 nCr 에 몇 개나 들어 있는지 세어주기 위한 배열 생성.
n! 에 들어 있는 해당 소수의 개수를 카운트하며, r!, (n-r)!에 들어 있는 소수의 개수만큼 빼주는 작업 진행.

이항 계수 = n!/(n-r)! r!  (mod M)
모듈러 연산의 분배법칙 
(A*B)%M = ((A%M) * (B%M)) % M

구현
1. N!에 대해 소수의 개수를 구함(에라토스테네스의 체 알고리즘 이용)
2. (N-K)! 과 K!에 대해서도 소수의 개수를 구함
3. 포함 배제의 원리 |A | B| = |A| + |B| - |A & B|
  (N-K)! 과 K!의 소수의 합집합 = (N-K)! 의 소수 + K!의 소수 - (N-K)!과 K!의 소수의 교집합
4. 모듈러 연산 과 소인수 분해
nCr (mod p)로 소인수 분해 => SUM i=1 (N/p^i - K/p^i - (N-K)/p^i)

예를 들어, N = 100, K = 46, M = 72라면,
1. N 에 대한 소수 리스트를 구한다.

'''

import sys
import math
from collections import defaultdict
input = sys.stdin.readline
N,K,M = map(int,input().split())

# 에라토스테네스의 체 알고리즘
def prime_number(n):  #  2 ~ n 까지의 소수 구하기
    pn = []
    array = {i:True for i in range(n+1)}
    array[0],array[1] = False,False
    for i in range(2, int(math.sqrt(n)) +1):
        if array[i] == True:    # i가 소수인 경우            
            j = 2
            while i*j <= n:
                array[i*j] = False
                j += 1

    for i in range(2,len(array)):
        if array[i]:
            pn.append(i)

    print(pn)            
    return pn

# N이 100인경우 25개의 소수가 포함됨
# 소인수 분해 정의에 의해 소수로 나
def calc_prime(p):
    np = defaultdict(int)
    for i in range(len(p)):        
        j = p[i]
        while j <= N:        
            np[i] += (N//j) - (K//j) - ((N-K)//j)
            j *= p[i]
    print(np)                
    return np        

p = prime_number(N)
np = calc_prime(p)

ans = 1
flag = False
for i in range(len(np)):
    for j in range(np.get(i)):
        ans *= p[i]
        ans %= M
        if ans == 0:
            flag = True
if flag:
    print('0')          
else:    
    print(ans)

'''
100 46 72

48
'''