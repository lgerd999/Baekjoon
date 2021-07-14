# https://www.acmicpc.net/problem/1620
# 참조 : https://blog.naver.com/hunii123/222314269485

from collections import defaultdict
import sys
input = sys.stdin.readline
'''
입력이 문자열일때,
sys.stdin.readline은 개행 문자까지 포함하여 입력을 받음
개행문자를 제거하기위해 rstrip()함수를 호출해야 함
단, 입력이 정수일때는 rstrip함수가 필요하지 않음

'''
poketmon = defaultdict(int)
M, mon = map(int,input().split())
for i in range(M):    
    data = input().rstrip()
    poketmon[data] = i+1
    poketmon[str(i+1)] = data

for j in range(mon):
    print(poketmon[input().rstrip()])
