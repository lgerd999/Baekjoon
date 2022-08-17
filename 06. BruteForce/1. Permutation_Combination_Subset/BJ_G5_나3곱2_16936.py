# https://www.acmicpc.net/problem/16936
#
'''
나3 : x를 3으로 나눈다. x는 3으로 나누어 떨어져야 함.
곱2 : x에 2를 곱한다.

4 8 6 3 12 9
4  : 2x2   --> x2 : 8 
8  : 2x2x2x2
6  : 2x3   --> x2 : 12     
3  : 3     --> x2 : 6 
12 : 2x2x3 --> /3 : 4
9  : 3x3   --> /3 : 3
-> 9 3 6 12 4 8

42 28 84 126
42 :   3x2x7
28 :   2x2x7
84 : 3x2x2x7
126: 3x3x2x7
-> 126 42 84 28

오른쪽으로  갈수록 3^n차수 감소, 2^n차수 증가

구현
1. 3과 2는 서로소이며, 3의 제곱이 클수록 첫번째 수가 되고 2의 제곱이 

'''
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
row = list(map(int,input().split()))

A = defaultdict(list)
for i in row:
    index = 0
    Q = i
    while Q % 3 == 0:
        Q = Q // 3
        index += 1
    
    A[index].append(i)
# print(A)
for i in range(max(A.keys()),-1,-1):    
    A[i] = sorted(A[i])
    for j in range(len(A[i])):
        print(A[i][j],end=' ')


'''
6
4 8 6 3 12 9

9 3 6 12 4 8
'''