# https://www.acmicpc.net/problem/21980
#
'''
n대의 자동차가 일렬로(좌->우) 주차. 이때 i 번째 자동차의 번호판 X[i]. 번호판 문자열의 길이 k
-- 모든 번호판의 길이는 같다.

임의의 자동차 번호판 X[i],X[j]가 다음 조건을 모두 만족하면 두 자동차는 비슷한 번호판을 가졌다고 판다.
-- 26가지의 각 알파벳에 대하여, 대/소문자를 무시했을 때 해당 알파벳이 x[i]에 적힌 횟수와 x[j]에 적힌 횟수가 같다 
    (이 조건은 각 알파벳에 대해 만족해야 한다).
-- x[i]에 적힌 대문자의 개수와 x[j]에 적힌 대문자의 개수가 같다.

n = 4, k = 3
X =[AtY,YtA,aTy,Ayt]
--> 1번과 2번차의 번호판은 비슷 : A/a 1 개, T/t 1개, Y/y 1개씩을 포함. 대문자는 3글자중 2글자.
--> 3번과 4번차의 번호판은 비슷 : A/a 1 개, T/t 1개, Y/y 1개씩을 포함. 대문자는 3글자중 1글자.
--> 1번과 3번차의 번호판은 비슷하지 않다 : 1번차는 대문자2개, 3번차는 대문자 1개 (첫번째 조건만 만족)

각 그룹에 속한 번호판의 개수를 알고 있다면, N개 중에서 순서 상관없이 뽑는 경우의 수
nCr = n!//(n-r)!r! 
nC2 = n!//(n-2)!2! = (n-1)*n//2

'''
import sys
# from itertools import combinations
from collections import defaultdict
input = sys.stdin.readline
                       
T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    char = list(map(str,input().split()))    
    # print('char=',char,combi_char)
    
    info = []        
    for c in char:                
        c_a = 0         
        ch = list(c)
        for i in range(k):
            if ch[i].isupper():
                c_a += 1    
                ch[i] = ch[i].lower()                                    
        
        info.append((c_a,''.join(sorted(ch))))
               
    cnt = defaultdict(int)                        
    for i in range(n):        
        cnt[info[i]] += 1
       
    # print(info,cnt)    
    ans = 0
    for i in cnt.values():
        ans += (i * ( i-1) //2)

    print(ans)        