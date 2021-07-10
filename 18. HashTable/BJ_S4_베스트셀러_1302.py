# https://www.acmicpc.net/problem/1302

N = int(input())

result = dict()
for _ in range(N):
    name = input()
    if name in result:
        result[name] += 1    
    else:    
        result[name] = 1
A = sorted(result.items(), key=lambda x:(-x[1],x[0]))
print(A[0][0])        
