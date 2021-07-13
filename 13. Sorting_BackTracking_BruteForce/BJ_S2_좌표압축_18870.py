# https://www.acmicpc.net/problem/18870

'''
    2 4 -10 4 -9
--> -10 -9 2 4 (4) 정렬하면 다음과 같고 중복되는 4는 제외
--> 2 앞에 2개가 있고, 4 앞에 3개가 있으며, -10 앞에는 0개, 4는 3, -9앞에는 1개
즉, 답은 2 3 0 3 1
'''
from collections import defaultdict,Counter
import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
data = list(map(int,input().split()))
A = Counter(data)
B = sorted(A.keys())
# print(A,B,sep=',')
ans = defaultdict(lambda:INF)
for i,j in enumerate(B):    
    if ans[j] == INF:
        ans[j] = i
    # print(ans)    

for i in data:
    print(ans[i], end = ' ' )
