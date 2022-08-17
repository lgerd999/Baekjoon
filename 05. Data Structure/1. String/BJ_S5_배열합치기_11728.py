# https://www.acmicpc.net/problem/11728
#
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
# data = []
# data.extend(list(map(int,input().split())))
# data.extend(list(map(int,input().split())))
data = sys.stdin.read().split()
# print(*sorted(data,key=int))
print(' '.join(sorted(data,key=int)))