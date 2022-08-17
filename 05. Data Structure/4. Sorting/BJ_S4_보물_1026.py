# https://www.acmicpc.net/problem/1026

N = int(input())
data = [list(map(int,input().split())) for _ in range(2)]
#print(data)
A = data[0]
A.sort()
B = data[1]
B.sort(reverse=True)
#print(A,B)

ssum = 0
for i in range(N):
    ssum += A[i]*B[i]

print(ssum)
