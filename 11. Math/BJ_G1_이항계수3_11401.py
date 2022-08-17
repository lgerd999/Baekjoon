# https://www.acmicpc.net/problem/11401
# 참고 : https://dailymapins.tistory.com/196
'''
이항계수2 문제 대비 N의 범위가 어마무시하게 넓어졌고 나눈 나머지도 엄청나게 값이 커졌다.
기존 DP를 이용하여 풀면 메모리 초과가 발생한다.
이를 해결하기 위해서는 아래의 방식으로 접근한다.

1. 모듈러 연산의 분배 법칙은 아래 3가지에 대해 성립.(나눗셈 제외)
(A+B)%C = (A%C + B%C)%C
(A-B)%C = (A%C - B%C)%C
(AxB)%C = (A%C x B%C)%C

2. 페르마의 소정리
p가 소수이고 a가 p의 배수가 아니면, a^p-1 = 1(mod p). 즉, a^p-1 을  p로 나눈 나머지는 1이다.
이는 임의의 소수 p와 서로소인 어떠한 수의 p-1 승을 p로 나눈 나머지는 무조건 1이라는 점.
예를 들어, 64^70(소수-1) 을 71(소수)로 나눈 나머지는 1이라고 순식간에 알 수 있음.

a^p-1 = a * a^p-2 = 1 , a^p-2 = a^-1 (mod p)
이는 a 의 역원이 a^p-2가 된다는 뜻.

결국, 이항계수 = (N!/(N-K)! K!) %p
페르마 소정리에 의해 분자 분모에 (N-K)! K! %p에 대한 역원을 구해서 분모를 1로 만들 수 있다.

1/(N-K)! K! = ((N-K)! K!)^-1 = ((N-K)! K!)^p-2 %p
A = (N-K)! K!
모듈러 연산의 곱셈 분배 법칙에 따라,
N!%p x (((N-K)!%p K!%p)^p-2)%p
를 구하는 문제로 바뀐다.

3. 분할 정복
거듭 제곱은 분할 정복이용. A^10 = A^5 x A^5

'''
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
p = 1000000007
'''
# 메모리 초과
C = [[0]*(N+2) for _ in range(N+2)]
C[0][0] = 1
for i in range(1,N+2):    
    for j in range(i):
        C[i][j] = (C[i-1][j-1] + C[i-1][j])%1000000007

# print(C)
print(C[N+1][K])
'''
def factorial(N):
    n = 1
    for i in range(2,N+1):
        n *= i
        n %= p
    return n    

def square(n,k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    sq = square(n,k//2)
    if k%2:
        return sq * sq * n % p
    else:
        return sq * sq % p
    
dem = factorial(N-K) * factorial(K) %p
# N!%p x (((N-K)!%p K!%p)^p-2)%p
print(factorial(N)*square(dem,p-2)%p)