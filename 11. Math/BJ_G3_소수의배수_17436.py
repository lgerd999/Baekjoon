# https://www.acmicpc.net/problem/17436
#
'''
포함-배제의 원리(집합의 교집합 크기를 구할 때 사용)
|A | B| = |A| + |B| - |A & B|
|A | B | C| = |A| + |B| + |C| - |A & B| - |A & C| - |B & C| + | A & B & C|
|A | B | C | D| = |A| + |B| + |C| - |A & B| - |A & C| - |B & C| + | A & B & C| + | A & B & D| + | A & C & D| + | B & C & D| - | A & B & C & D|

즉, 짝수개는 빼고, 홀수개는 더한다.

예) 100, 소수 = 2,3,5(A,B,C)
2 & 3 = 6, 2 & 5 = 10, 3 & 5 = 15, 2 & 3 & 5 = 30
100 / 2 = 50 +
100 / 3 = 33 +
100 / 5 = 20 +
100 / 6 = 16 -
100 /10 = 10 -
100 /15 = 6 -
100 /30 = 3 +
----------------
103 - 32 + 3 = 74

예) 100, 소수 = 2,3,5,7 (A,B,C)
100 / 2 = 50 +
100 / 3 = 33 +
100 / 5 = 20 +
100 / 7 = 14 +
100 / 6 = 16 -
100 /10 = 10 -
100 /15 = 6 -
100 /14 = 7 -
100 /21 = 4 -
100 /35 = 2 -
100 /30 = 3 +
100 /42 = 2 +
100 /70 = 1 +
100 /105 X(-)
100 /210 X(+)
----------------
117 - 19 + 6 = 78

구현
1.

'''
import sys
from itertools import combinations
input = sys.stdin.readline


# 입력 : 소수, 출력 : 소수의 교집합

def combi(pn):
    if len(pn) == 1:
        return -1,-1
    even = []
    odd = []        
    for i in range(2,len(pn)+1):        
        cnr = list(combinations(pn,i))        
        
        for j in range(len(cnr)):
            mul = 1
            for k in range(i):
                mul *= cnr[j][k]
            if i%2 == 0:    
                even.append(mul)
            else:
                odd.append(mul)    
              
    # print(even,odd)  
    return even,odd
          

N,M = map(int,input().split())
pn = list(map(int,input().split()))

# M//소수    
ans = 0
for i in pn:
    ans += M//i

# 교집합 처리
e,o = combi(pn)
if e != -1 and o != -1:
    if e: # 짝수 번째
        for i in e:
            ans -= M//i
    if o:   # 홀수 번째
        for i in o:
            ans += M//i
print(ans)


