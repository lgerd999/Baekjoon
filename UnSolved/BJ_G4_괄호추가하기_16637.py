# https://www.acmicpc.net/problem/16637
#
'''
N이 최대 19이면 연산은 최대 18개
+,-,* 연산식에서 괄호를 묶어서 최대값을 만들기.
조건1. 연산 우선 순위는 모두 동일.
   -- 덧셈/뺄셈 연산을 먼저하고 곱셈하는게 가장 최대값.
   -- 덧셈/뺄셈 연산 후 반드시 곱셈 연산이 와야 함.
조건2. 괄호안에는 연산자가 하나만 들어 있어야 한다.

예) 3+8*7-9*2의 경우의 수 이중 최대값 선택
 --> (3+8)*7-9*2 = 136 (덧셈 연산이 우선순위)
 --> (3+8)*(7-9)*2
 --> (3+8)*7-(9*2)
 --> 3+(8*7)-9*2
 --> 3+(8*7)-(9*2)
 --> 3+8*(7-9)*2
 --> 3+8*7-(9*2)
8*(3+5)+2
1*(2+3)*4*5-6*7*8*9*0
1-9-(1-9)-(1-9)-(1-9)-(1-9)
--> -8 + 8 + 8 + 8 +8 = 24

구현
1. 괄호는 우선순위가 가장 높다. 어떻게 우선 순위를 부여할 것인가. 괄호의 개수 조합.
  -- 연산 부호를 dict으로 정의. {'*': index} 로 지정. 
  -- 연속된 부호에서 괄호가 올 수 없다. 
   예를 들어, 부호의 개수가 4개 라면,
   [+ * - *]는 +,- 또는 *,*에만 괄호
   -- +    (0)
   -- +,-  (0,2)
   -- +, * (0,3)
   -- -    (2)
   -- *(앞) (1)
   -- *, *  (1,3)
   -- *(뒤) (3) 
   --> 0,1,2,3,(0,2),(1,3)
   
   
'''

import sys
from itertools import combinations
input =sys.stdin.readline

def calc(num,op):
   ans = 0
   oper = op.pop()
   while op:
      n1,n2 = num.pop(0),num.pop(0)      
      if oper == '+':
         ans = n1 + n2
      elif oper == '-':
         ans = n1 - n2
      elif oper== '*':      
         ans = n1 * n2

N = int(input())
S = list(input().rstrip())
num = []
op = []
for i in range(N):   
   if S[i] == '*' or S[i] == '+' or S[i] == '-' :
      op.append(S[i])
   else:
      num.append(S[i])      

# 괄호 조합
braket = []
for c in combinations(range(len(op)),2):
   if len(c) == 2 and abs(c[0] - c[1]) == 1:
      continue
   braket.append(c)

print(braket)         

# 계산 
# 괄호 우선



# print(op,num)
