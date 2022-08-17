# https://www.acmicpc.net/problem/10814
#
import sys
input = sys.stdin.readline

N = int(input())
member = []
for i in range(N):
    age, name = map(str,input().split())
    member.append([i,int(age),name])
print(member)
for i in sorted(member,key=lambda x: (x[1],x[0])):
    print(*i[1:])