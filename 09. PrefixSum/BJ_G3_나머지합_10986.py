# https://www.acmicpc.net/problem/10986
# 참조 : https://zoosso.tistory.com/550
# https://www.acmicpc.net/problem/2015 유사한 문제
'''
연속된 부분의 구간의 합이 M으로 나누어 떨어지는 구간의 개수 구하기

예) 수열 = 1 2 3 1 2, M = 3

1+2 =3
1+2+3 = 6
1+2+3+1+2 = 9
2+3+1 = 6
3+1+2 = 6
1+2 = 3
3 (문제에서 i = j도 포함)  <-- 1개

i             : 0 1 2 3 4 5
array[i]      :   1 2 3 1 2    
S[i]          : 0 1 3 6 7 9  --> [0:2],[0:3],[1:4],[2:3],[2:5],[3:5]
S[i]%3        : 0 1 0 0 1 0
cnt = 3 2 0

'''

import sys
from math import ceil,log2
input = sys.stdin.readline

N,M = map(int,input().split())
array = list(map(int,input().split()))

#누적합
'''
S[i] = A[1]+ ...+A[i-1] + A[i]
A[i]+...+A[j] = S[j] - S[i-1]
(A[i]+...+A[j])%M = (S[j]-S[i-1])%M
==> (A[i]+...+A[j])%M == 0인 것의 개수를 구해야 함. 이는 (S[j]-S[i-1])%M == 0의 개수를 구하는 것과 같음.
==> S[j]%M == S[i-1]%M
'''
S = [0]*(N+1)
cnt = [0]*M
for i in range(1,N+1):
    S[i] = S[i-1] + array[i-1]
    # 구간의 합을 M으로 나눈 나머지가 같은 것 끼리 분류
    cnt[S[i]%M] += 1

print(S,cnt)

# 나머지가 같은 것들 중 임의로 2개를 선택하는 방법 : nC2 = n!//2!(n-2)! = n * (n-1)//2
'''
1 1 0 1 1 이라면 1의개수 4개로 만들 수 있는 구간의 개수는 nC2
==> (0 1),(0 3),(0 4),(1 3), (1 4), (3 4)
'''
ans = cnt[0]
for i in cnt:
    if i:
        ans += i * (i-1) //2
    
print(ans)    

