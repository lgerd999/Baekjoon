#https://www.acmicpc.net/problem/12919
# 비슷한 유형 : https://www.acmicpc.net/problem/12904
'''
연산1. 문자열의 뒤에 A를 추가한다.
연산2. 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.

기존 A와 B 문제와 차이점
-- 문자열을 뒤집고 뒤에 B를 추가한다. --> 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.

예) S -> T
S = A
T = BABA
---------
T에 대해 역순으로 연산하면,
BABA ==> 마지막 글자가 A. 연산1 이라면, BAB, 연산2 라면, ABA 
  BAB --> 연산2이므로 BA
     BA --> 마지막 글자가 다시 A. 연산1 이라면 B, 연산2 라면 A
  ABA --> 연산 1이므로 AB. 
     AB --> 연산1도 아니고, 연산2도 아님.

예2) A
ABBA
--------
ABBA ==> 연산1이므로 ABB
  ABB ==> 연산1도 아니고 연산2도 아니다.

구현상 문제점
-- BA가 남은 시점에 마지막이 A이므로 A연산인지... 역순으로 보면 B가 마지막이니 B연산인지...  이부분 처리 필요.
--> S의 시작 문자가 A이면, BA가 남은 시점에는 B연산으로 처리.

'''
import sys
input = sys.stdin.readline

def search(ans):
    global flag
    
    if len(ans) == len(S):
        if ans == S:
            flag = True
        return
    
    # 연산2 수행 : B를 추가하고 뒤집었기 때문에 문자열 제일 앞에 B가 있어야 함.
    if ans[0] == 'B':   
        ans = ans[::-1] 
        ans.pop()                
        print('op2',ans)
        search(ans)
        ans.append('B') # 연산2 수행 전으로 복원 (연산1 계산을 위해)
        ans = ans[::-1] 
    # 연산1   
    if ans[-1] == 'A':           
        ans.pop()        
        print('op1',ans)
        search(ans)
        ans.append('A')
       
S = list(input().rstrip())
T = list(input().rstrip())

flag =False

search(T)

if flag:
    print(1)
else:
    print(0)    
