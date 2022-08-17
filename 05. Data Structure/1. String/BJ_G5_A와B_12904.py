# https://www.acmicpc.net/problem/12904
#

import sys
# from collections import deque
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()
'''
# BFS를 이용한 탐색 : 메모리 초과
def bfs():
    Q = deque()
    Q.append(S)
    while Q:
        r = Q.popleft()
        # print(r)
        if r == T:
            return True
        if len(r) > len(T):
            return False
            
        for n in (r + 'A', r[::-1] + 'B'):
            Q.append(n)
        
    return False

if bfs():
    print(1)
else:
    print(0)    
'''
'''
문제가 S를 T로 바꿀 수 있는지 여부를 물어봄
- A연산 : 문자열의 뒤에 A를 추가
- B연산 : 문자열을 뒤집고 그 뒤에 B를 추가

S를 T로 바꿀려고 보니 경우의 수가 2^999 이므로 단순화가 필요
--> 역으로 T를 S로 바꿔보기
예) S: B, T:ABBA
ABBA : 뒤에 A가 있으므로 A연산. (문자열 뒤 A만 삭제)
--> ABB : 뒤에 B가 있으므로 B연산.(B를 삭제하고 문자열 뒤집기)
--> BA :A연산이므로 A만 제거
--> B : S로 변경 가능.

'''
ans = list(T)
flag =False
while ans:
    if ans[-1] == 'A':
        ans.pop()
    elif ans[-1] == 'B':
        ans.pop()
        ans = ans[::-1]   
    if  "".join(ans) == S:
        flag = True
    # print(ans)

if flag:
    print(1)
else:
    print(0)    
