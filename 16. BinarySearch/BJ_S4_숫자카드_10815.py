# https://www.acmicpc.net/problem/10815

from collections import Counter

N = int(input())
card = list(map(int,input().split()))
M = int(input())
data = list(map(int,input().split()))

card_list = Counter(card)
#print(card_list)

for i in range(M):
    print(card_list[data[i]],end=' ')