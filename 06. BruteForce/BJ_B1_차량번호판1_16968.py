# https://www.acmicpc.net/problem/16968
# 브루드포스 
'''
차량 번호판 4자리로 숫자와 문자 조합으로 구성.
입력으로 자리수가 주어질 때 가능한 번호판 개수 구하기
 - 문자와 숫자, 숫자와 숫자, 문자와 문자로 구성
 - 문자와 문자, 숫자와 숫자는 같은 문자, 같은 숫자가 2번 연속한 구성은 불가
 - 예를 들어, dd면 10x10 - 중복수 = 90, cc 면 26 x 26 - 26 = 650, 
    연속해서 나타나는 경우 dd = 10*(10-1), ddd = 10 *(10-1)*(10-1) = 810
    dcdd = 10 x 26 x 10 x 9 = 23400
             
'''
import sys
input = sys.stdin.readline

car = list(input().rstrip())

result = 10 if car[0] == 'd' else 26
for i in range(1,len(car)):
    if car[i] == 'c':
        if car[i-1] == 'c':
            result *= 25
        else:
            result *= 26
    else:            
        if car[i-1] == 'd':
            result *= 9
        else:
            result *= 10

print(result)