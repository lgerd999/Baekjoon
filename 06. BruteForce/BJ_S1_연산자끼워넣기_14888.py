# https://www.acmicpc.net/problem/14888

from itertools import permutations
import sys

N = int(input())
data = list(map(int,input().split()))
operator = list(map(int,input().split()))
#print(data,operator)

'''
구현 아이디어
1. 연산자(+,-,x,/)를 숫자로 치환하여 O 변수에 저장
2. 연산자의 경우의 수의 조합을 순열을 이용해서 구한다. 단 중복이 있을 수 있기 때문에 set함수를 이용하여 중복을 제거해 준다.
3. 순열을 이용해서 연산을 수행한다. 이중 최소/최대를 업데이트한다.
'''
# 1 : +, 2 : -, 3 : X, 4 : / 연산
O = []
for i in range(4):
    if operator[i]:
        for _ in range(operator[i]):    
            O.append(i+1)
#print(O)     


if len(O) > 1:
    A = list(set(permutations(O,len(O))))   # 중복 제거를 위해 set 사용
else:
    A = [O] 
print(A)

# 문제에서 출력 범위가 -10억에서 +10억 사이로 되어 있음
min_ = 1000000000
max_ = -1000000000

for i in range(len(A)):
    ssum = data[0]    
    for j in range(len(A[i])):       
        if A[i][j] == 1:
            ssum += data[j+1] 
        elif A[i][j] == 2:
            ssum -= data[j+1]
        elif A[i][j] == 3:                    
            ssum *= data[j+1]
        elif A[i][j] == 4:    
            # 나눗셈은 정수 나눗셈 몫만 취함
            # 단, 음수를 양수로 나눌 때 C++ 14기준을 따르는데 이는 양수로 바꾼 뒤 몫을 취하고 그 몫을 다시 음수를 바꾼다.
            # 예를 들어, -1//3 = -1 이지만, 1//3 = 0이므로 위와 같은 계산을 한다.
            if ssum < 0:                
                ssum = ((ssum* (-1)) // data[j+1]) * (-1)
            else:          
                ssum //= data[j+1]      
            
    min_ = min(min_,ssum) 
    max_ = max(max_,ssum)
print(max_)    
print(min_)    

