# https://www.acmicpc.net/problem/1208
# 
'''
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 문제

예)
5 0
-7 -3 -2 5 8 
==> 모든 조합의 개수는 2^5이며, 최대 N이 40까지 가능하므로 경우의 수가 2^40까지 나올 수 있다.
(-7,-3)(-7,-2)(-7,5)(-7,8),(-7,-3,-2)(-7,-3,5)(-7,-3,8),(-7,-3,-2,5)(-7,-3,-2,8),(-7,-3,-2,5,8) :10개
(-3,-2)(-3,5)(-3,8),(-3,-2,5)(-3,-2,8),(-3,-2,5,8) : 6개
(-2,5)(-2,8),(-2,5,8) : 3개
(5,8) ; 1개
==> 각 부분 수열의 각각의 원소의 합이 S(=0)가 되는 경우의 수는 1개

구현
1. 최대 2^40까지 나오면 시간초과가 발생한다. 
2. 배열을 반으로 나누면 최대 2^20까지이므로 시간 초과를 피할 수 있다.
  ==> 배열 array를 반으로 나누면 A = array[:N//2],B = array[N//2:]의 새로운 배열이 생성된다.
  ==> combination을 이용하여 부분집합의 경우의 수를 뽑고 각 경우의 수들의 합들에 대해 카운팅(result)
3. S값을 만족하는 left,right, left+right 조합을 구한다.

'''

import sys
from itertools import combinations
from collections import defaultdict

input = sys.stdin.readline

def sub_sum(A):
# 부분 수열의 합의 결과를 result라는 딕셔너리에 저장    
    result = defaultdict(int)
    for leng in range(1,len(A)+1):
        for combi in combinations(A,leng):            
            result[sum(combi)] += 1       
    return result

N,S = map(int,input().split())
array = (list(map(int,input().split())))
# print(array)

left = sub_sum(array[:N//2])
right = sub_sum(array[N//2:])
print(left,right)                

# 왼쪽 단독, 오른쪽 단독으로 S값을 만족하는 값
ans = left[S]+right[S]
# 왼쪽과 오른쪽의 조합으로 S값을 만족하는 부분 카운팅
for l in left:
    if S-l in right:
        ans += left[l]*right[S-l]        

print(ans)



