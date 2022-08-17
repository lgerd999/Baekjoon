# https://www.acmicpc.net/problem/16943
# 브로드포스
'''
A와 B 가 있을 때 A에 포함된 숫자의 순서를 섞어서 새로운 수 C를 만든다.
이때 C는 A의 순열 중 하나이며, C중에서 B보다 작으면서, 가장 큰 값을 구하는 문제
'''
from itertools import permutations
import sys
input = sys.stdin.readline

A,B = input().rstrip().split()

new_A = list(A)
result = []
for a in permutations(new_A,len(new_A)):
    C = int(''.join(map(str,a))) 

    if  C < int(B) and len(str(C)) == len(new_A):
        result.append(C)
# print(result)
if result:        
    print(max(result))        
else:
    print(-1)        