# https://www.acmicpc.net/problem/4358

import sys
input = sys.stdin.readline

tree = dict()
cnt = 0
while True:
    name = input().rstrip()
    if not name :
        break
    cnt += 1
    if name in tree:
        tree[name] += 1
    else:
        tree[name] = 1
    
print(tree) 
A = sorted(tree.items(),key=lambda x:x[0])
for i,j in A:
    print('{0} {1:0.4f} '.format(i,(j/cnt)*100))

