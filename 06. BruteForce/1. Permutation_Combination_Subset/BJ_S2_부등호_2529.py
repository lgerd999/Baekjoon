# https://www.acmicpc.net/problem/2529
#
'''
부등호가 주어졌을 때 0~9사이의 수 중 조건을 만족하는 수 중 최대값과 최소값 찾기

예를 들어, < >라면,
첫번째 조건 < 를 만족하는 수는 아래와 같다.
0<1 ~ 9
1<2 ~ 9
2<3 ~ 9
...
8 < 9 
두번째 조건 > 라면,
0<2>1, 0 <3>2, ... 최소값은 021
1<2 는 1 < 2 > 0 ... 하지만 최소값은 아니고, 현재 최대값은 되지만 구하고자 하는 최대값은 8로 시작하는 것에 있을 것이라 유추가 가능.
2<3 ... 
...
8<9>0...7 최대값은 897

구현
예) > < < < > > > < <  ==> '>'(A):4, '<'(B) : 5 
1. 최대값을 구하기 위해 주어진 부등호의 첫번째 값을 살펴본다.
   > 라면, 9로 시작하는 값이 최대값, 1로 시작하는 값이 최소값. 9와 1은 삭제. 0,2~8 까지 사용 가능
2. 다음 부등호가 몇 개가 있는지 확인. B가 5개 있음. 
   > 라면, 9>
   < 라면, 9> 9-(B-1) <                     9-(B-1). 5는 삭제. 0,2~4,6~8
   < 라면, 9> 5 < 9-(B-2) <                 9-(B-2). 6는 삭제. 0,2~4,7~8
   < 라면, 9> 5 < 6 < 9-(B-3) <             9-(B-3). 7는 삭제. 0,2~4,8
   > 라면, 9> 5 < 6 < 7 < 9-(B-4) >         9-(B-4). 8은 삭제. 0,2~4
   > 라면, 9> 5 < 6 < 7 < 8 > 4              
   > 라면, 9> 5 < 6 < 7 < 8 > 4 >            
   > 라면, 9> 5 < 6 < 7 < 8 > 4 > 2 < 3           

'''
import sys
from itertools import permutations
input = sys.stdin.readline

k = int(input())
sign = list(map(str,input().split()))

def check(P):
    ans = []
    for p in permutations(P,k+1):
        flag = True
        for i in range(k):            
            if sign[i] == '<':
                if p[i] < p[i+1]: continue
                else:
                    flag = False
                break 
            else:
                if p[i] > p[i+1]: continue
                else:
                    flag = False
                break                
        if flag :
            ans.append(p)
    # print('check',ans)
    return ans
P = [i for i in range(10)]
# permutations의 특성상 0~9까지 오름차순으로 진행하기 때문에 첫번째 값이 최소값이 되고 마지막 값이 최대값이 된다.
ans = check(P)
min_value = ans[0]
max_value = ans[-1]
print(''.join(map(str,max_value)))
print(''.join(map(str,min_value)))

