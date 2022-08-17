# https://www.acmicpc.net/problem/1541
#
'''
괄호를 적절히 쳐서 값을 최소로 만드는 문제
- '+','-' 기호와 숫자만 입력
- 값이 최소가 되기 위해서는 '-' 기호 다음 수가 '+'가 있는 경우를 찾는다.
- 같은 기호는 그냥 패스 

'''

import sys
input = sys.stdin.readline

Minus = input().rstrip().split('-')

ans = 0
for i in range(len(Minus)):
    Plus = list(Minus[i].split('+'))
    # print(Plus)

    Sum = 0
    for j in Plus:
        Sum += int(j)
    if i == 0:
        Sum = -Sum
    ans -= Sum

print(ans)    

'''
# 내가 푼 방식
E = input().rstrip()

num = []
index = 0
for i in range(len(E)):
    if E[i] == '+' or E[i] =='-':
        num.append(int(E[index:i]))
        index = i
    if i == len(E)-1:
        num.append(int(E[index:]))    

flag = False        
ans = 0
for i in num:
    if i < 0 and not flag:
        flag = True
    elif i < 0 and flag:
        pass    
    else:
        if flag:
            i = -i
    # print(i)        
    ans += i    
print(ans)
'''
'''
0-8994+8+00-610+722+6691-482+65-3
--> -8994(T), -8(T),0(T),-610(P),-722(T),-6691(T),-482(P),-65(T),-3(P)
-17575


'''