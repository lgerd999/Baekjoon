# https://www.acmicpc.net/problem/1253

N = int(input())
data = list(map(int,input().split()))
data.sort()

cnt = 0
for i in range(N):    
    A = data[:i]+data[i+1:] # 데이터에서 0과 자기 자신의 값을 제외
    
    '''
    A의 길이는 전체 길이 -1(자기자신)만큼 뺀수, 두수의 합에 목표 값이 포함되지 않게 하기 위함    
    i = 1, A[1] = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    i = 2, A[2] = [1, 3, 4, 5, 6, 7, 8, 9, 10]
    ...
    i = 10, A[10] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
    left,right = 0,len(A)-1
    while left < right:
        summ = A[left]+A[right]
        if summ == data[i]:     # 목표(data[i])와 두 수의 합이 같으면, count 계산
            print(A[left],A[right])
            cnt += 1            
            break
        if summ < data[i]:    # 두 수의 합이 목표값보다 작으면, left +1 이동 (참고: 오름차순 정렬됨)
            left += 1    
        else:
            right -= 1                  
    
print(cnt)        