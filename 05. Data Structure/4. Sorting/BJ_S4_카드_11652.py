# https://www.acmicpc.net/problem/11652
# Counter의 most_common 메소드를 이용해서 해결

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
data = [int(input().rstrip()) for _ in range(N)]
data.sort()
print((Counter(data).most_common(1))[0][0])