# https://www.acmicpc.net/problem/2776
#
'''
동규 : 하루동안 본 정수들을 수첩1에 기록
동규는 연종에게 M개의 질문을 함
동규는 연종이 봤다고 주장하는 수들을 수첩2에 기록
수첩2에 적혀있는 순서대로 수첩1에 있으면 1, 없으면 0

'''
import sys
from bisect import bisect_left,bisect_right
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    n1 = list(map(int,input().split()))
    n1 = sorted(n1)    
    M = int(input())
    note2 =  list(map(int,input().split()))
    for i in note2:
        idx = bisect_left(n1,i)
        if idx < N and n1[idx] == i:
            print(1)
        else:
            print(0)    
    