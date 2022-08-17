# https://www.acmicpc.net/problem/14225
import sys
from collections import defaultdict
input = sys.stdin.readline

def sum(index,path):
    # print(index,path)
    ans[path] = 1

    for i in range(index,N):
        sum(i+1,path + S[i])
    

# N은 1보다크거나 같고 20보다 같거나 작다.
N = int(input())        
S = list(map(int,input().split()))

ans = defaultdict(int)

sum(0,0)

# print(ans)

for i in range(len(ans.keys())):    
    if ans[i] != 1:
        print(i)
        exit(0)

    
print(i+1)    

