# https://www.acmicpc.net/problem/10816

from collections import Counter
N = int(input())
data = list(map(int,input().split()))
M = int(input())
card = list(map(int,input().split()))

A = Counter(data)
#print(A)

result = []
for i in card:
    result.append(A[i])
print(*result)    