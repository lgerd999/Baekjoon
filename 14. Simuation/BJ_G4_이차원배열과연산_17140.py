# https://www.acmicpc.net/problem/17140
# 정렬, Counter, Zip, Dictionary, Stack 다양한 함수 적용

from collections import Counter,defaultdict
'''
구현 아이디어(operation 함수)
1. Counter 함수를 이용하여 각 행 또는 열의 수가 몇 번 나왔는지 계산
2. 계산된 값은 Stack R에 key, value로 저장(이때 extend로 저장하고 0은 제외)
3. 저장된 값은 정렬 함수를 이용
4. 각 행의 열의 값이 다른 경우 0값을 패딩해 주어야 함
'''
def operation(grid):
    max_r = 0
    R = [[] for _ in range(len(grid))]
    cnt = defaultdict(int)
    for i in range(len(grid)):
        cnt = Counter(grid[i])
        S = dict(sorted(cnt.items(),key=lambda x:(x[1],x[0])))                    
        for j,k in S.items():
            if j:
                R[i].extend([j,k])                        
        max_r = max(max_r,len(R[i]))
    
    for i in range(len(R)):
        from_ = len(R[i])        
        R[i].extend([0 for _ in range(from_,max_r)])        
    return R

# R연산인지 C연산인지 체크하는 함수   
def check_operation(grid):
    if len(grid) >= len(grid[0]):
        return 1 # R 연산
    return 0       # C 연산

r,c,k = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(3)]
cnt = 0  

# 카운트가 100을 넘어가면 안됨
while cnt <= 100:    
    # data 값이 A[r][c] = k 인 경우 출력하고 나감
    # 이때 r-1, c-1값이 원 데이터보다 작으면 안되는 조건 추가해야 index error 발생 안함
    if len(data[0]) > c-1 and len(data) > r-1 and data[r-1][c-1] == k:
        break   
    if check_operation(data):
        data = operation(data)
    else:
        # zip 함수는 행 <->열 변환가능        
        B = list(zip(*data))  # 행 --> 열 변환
        C = operation(B)  #    연산 및 정렬
        data = list(zip(*C))  # 열 --> 행 변환
#    print(data)    
    cnt += 1
 
if cnt > 100:
    print(-1)    
else:    
    print(cnt)    

