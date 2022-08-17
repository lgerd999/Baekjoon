import sys
from itertools import combinations
from collections import defaultdict

input = sys.stdin.readline

def sub_sum(A):
# 부분 수열의 합    
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
#print(left,right)                

ans = left[S]+right[S]
for l in left:
    if S-l in right:
        ans += left[l]*right[S-l]        

print(ans)