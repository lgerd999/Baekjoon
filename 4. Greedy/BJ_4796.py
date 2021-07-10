L,P,V = map(int,input().split())
ans = []
while L and P and V:
    Q,R = divmod(V,P)  # Q : 1개 이상의 연속된 캠핑 일자        
    ans.append(Q*L + min(R,L))    
    
    L,P,V = map(int,input().split())

for i in range(len(ans)):
    print('Case',str(i+1)+':',ans[i])    