T = int(input())

e=[300,60,10]

result = []
for i in e:
    Q,R = divmod(T,i)
    result.append(Q)
    T = R
if T == 0:
    print(*result)    
else:
    print(-1)    