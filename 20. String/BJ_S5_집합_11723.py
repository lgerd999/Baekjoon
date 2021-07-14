# https://www.acmicpc.net/problem/11723
'''
집합을 이용한 문제
'''
import sys
input = sys.stdin.readline

M = int(input())
S = set()
Allo = {i for i in range(1,21)}

for _ in range(M):    
    data = input().split() # 리스트 형태로 입력

    # 입력이 2개일때, 1개일 때 구분
    oper = data[0]
    if len(data) == 2:        
        num = int(data[1])
    
    if oper == 'add':
        if 1 <= num <= 20:
            if num not in S:
                S.add(num)
    elif oper == 'remove':    
        if 1 <= num <= 20:
            if num in S:               
                S.remove(num)
    elif oper == 'toggle':
        if num in S:
            S.remove(num)    
        else:
            S.add(num)    
    elif oper == 'all':
        S.update(Allo)        
    elif oper == 'empty':
        S = set()    
    elif oper == 'check':
        if 1 <= num <= 20:
            if num in S:
                print(1)    
            else:
                print(0)    



