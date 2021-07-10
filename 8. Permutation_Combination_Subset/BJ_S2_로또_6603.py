# https://www.acmicpc.net/problem/6603

from itertools import combinations

data = list(map(int,input().split()))
A = []
while data != [0]:
    A.append(list(combinations(data[1:],6)))    
    data = list(map(int,input().split()))
    #print()

for i in range(len(A)):
    for j in range(len(A[i])):
        print(*A[i][j],end=' ')    
        print()
    print()    