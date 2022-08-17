# https://www.acmicpc.net/problem/12970
#
'''
문자열 S의 길이는 N이고 A와 B로 구성.
S[i] == 'A' and S[j] == 'B'를 만족하는 (i,j)쌍이 K개 있다. (0<= i < j < N)

N = 3라면, K는 다음과 같다. (A의 개수 a, B의 개수 b)
AAA 또는 BBB => 총 0
BBA => 0
BAB => 총 1개쌍(1,2)
ABB => 총 2개쌍(1,2),(1,3)
AAB => 총 2개쌍(1,3),(2,3)

(A,B)쌍의 개수 0 ~ axb(a=1,b=2/a=2,b=1) (MAX K=2)

N = 4라면, K는 다음과 같다.
AAAA 또는 BBBB => 총 0
BBBA => 0
BBAB => 총 1개쌍(3,4)
BABB => 총 2개쌍(2,3),(2,4)
ABBB => 총 3개쌍(1,2),(1,3),(1,4)
AABB => 총 4개쌍(1,3),(1,4),(2,3),(2,4)
AAAB => 총 3개쌍

(A,B)쌍의 개수 0 ~ axb(a=2,b=2) (MAX K=4)

N = 5라면, K는 다음과 같다.
AAAAA 또는 BBBBB => 총 0
BBBBA => 0
BBBAB => 총 1개쌍
BBABB => 총 2개쌍
BABBB => 총 3개쌍
ABBBB => 총 4개쌍
AABBB => 총 6개쌍
AAABB => 총 6개쌍
ABABB => 총 5개쌍
AABAB

(A,B)쌍의 개수 0 ~ axb(a=2,b=3/a=3,b=2) (MAX K=6)

3가지 경우를 살펴보면 (A,B)쌍의 최대 개수는 axb 일때이다.(axb = MAX K, 주어진 K에 대해서는 axb >= K를 만족해야 한다.)
여기서 우리는 K가 주어졌을 때 (A,B)쌍이 최대가 되는 a와 b의 개수를 구해야 한다.

구현
1. 시작은 앞에 A를 두고 나머지를 B로 채운 길이 N부터 시작한다. ABBB...
 -- A는 (a-1)개를 사용하였기 때문에, 0 ~ (a-1)xb 만큼의 K 쌍이 발생한다.
 -- a = N/2일 때 최대. b = N - a 
2.주어진 K가 있다면, K - (a-1) x b 위치에 A를 넣으면 된다. 
 -- N = 5, K = 3이라면, ABBB(N-1) => (a-1) xb = 3, 3 - 3 = 0, 왼쪽에서 인덱스 : (N-1) - 0 = A의 위치(4), ABBBA가 답.
 -- N = 10, K = 12 라면, ABBBBBBBB(N-1) => (a-1) xb = 8, 12 - 8 = 4, 왼쪽에서 인덱스 : (N-1) - 4 = A의 위치, ABBBBABBBB가 답. BAABBABAAB 
3. N과 K가 주어졌을 때, N
  -- a가 N//2, b = N - a, 최대 K = a*b
  -- N = 7, K = 12 라면, 
    ABBBBBB ==> 6,    ABBBBBA ==> 5,    ABBBBAB ==> 6,    ABBBABB ==> 7,    ABBABBB ==> 8,    ABABBBB ==> 9,    
    AABBBBB ==>10,    AABBBBA ==> 8,    AABBBAB ==> 9,    AABBABB ==> 10,   AABABBB ==> 11,,  AAABBBB ==> 12(MAX K)
 
    a가 0,7일때, K는 0, AAAAAAA,BBBBBBB
    a가 1,6일때, K는 최대 6,  ABBBBBB,AAAAAAB, 1*6
    a가 2,5일때, K는 최대 10, AABBBBB,AAAAABB, 2*5
    a가 3,4일때, K는 최대 12, AAABBBB,AAAABBB, 3*4
    
'''
import sys
input = sys.stdin.readline

N,K = map(int,input().split())

ans = ['B']*N
a = 0
mK = 0
# 주어진 K에 대한 a 값 선정. 
# N//2가 1일때 for문을 진입하지 못해 1일때는 2로 설정.
if N//2 == 1:
    max_a = 2
else:    
    max_a = N//2

# K는 0보다 크고 a*b <= K 일때, 앞의 A의 갯수를 구하기 위함   
for i in range(1,max_a):    
    if i * (N-i) <= K and K > 0:   
        a = i                
        ans[i-1] = 'A'
        mK = a*(N-a) - i               
        # print(i,ans,a,mK)

index = N - (K-mK) - 1
if index > -1 and ans[index] != 'A':
    ans[index] = 'A'
    a += 1
# print(ans,index,a,N-a)            
b = N - a

if a*b >= K:
    print(''.join(map(str,ans)))        
else:
    print('-1')    

