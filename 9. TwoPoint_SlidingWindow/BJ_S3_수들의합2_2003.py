N,K = map(int,input().split())
data = list(map(int,input().split()))

#방법1 - 미리 합을 구해서 계산하는 방식(pypy만 pass됨)
# table = [0] * N
# for i in range(N):
#     table[i] = sum(data[:i+1])
# print(table)    
# cnt = table.count(K)
# for i in range(N+1):
#     for j in range(i,N):
#         val = table[j] - table[j-i]
#         print(j,j-i)
#         if val == K:
#             cnt += 1
# print(cnt)            

#방법2 - two point 방식
'''
구현 아이디어
1. left와 right에 해당하는 데이터를 더한 값이 K보다 작으면 right를 하나 증가시켜 본다.
2. 이 값이 K와 같다면, 다음에는 left, right를 모두 하나씩 증가시킨다.
3. 만약 1번에서 증가시킨 값이 K보다 크다면 left를 증가시켜서 K값을 줄여본다.
'''
left,right = 0,0
cnt=0
while left <= right <= len(data):
    summ = sum(data[left:right])
    print(left,right,summ)
    if summ == K:
        cnt += 1
    if summ < K:    
        right += 1
    elif summ > K: 
        left += 1        
    else:
        left += 1
        right += 1
print(cnt)