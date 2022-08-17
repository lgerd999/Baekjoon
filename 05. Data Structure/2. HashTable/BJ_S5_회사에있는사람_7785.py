# https://www.acmicpc.net/problem/7785

import sys
input = sys.stdin.readline

result = dict()
N = int(input())
for _ in range(N):
    name, IO = map(str,input().split())
    if IO == 'enter':
        if name not in result:
            result[name] = 1
    elif IO == 'leave':
        if name in result:
            del result[name]
print(*sorted(result.keys(),reverse=True),sep='\n')
