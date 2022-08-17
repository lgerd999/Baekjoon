# https://www.acmicpc.net/problem/10825
#

import sys
input = sys.stdin.readline

N = int(input())
member = []
for i in range(N):
    name,K,E,M = map(str,input().split())
    member.append([name,int(K),int(E),int(M)])
    
for i in sorted(member,key=lambda x:(-x[1], x[2],-x[3],x[0])):
    print(i[0])