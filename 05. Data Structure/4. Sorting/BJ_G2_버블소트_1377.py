# https://www.acmicpc.net/problem/1377
# 참고 : https://infinitt.tistory.com/229
'''
* 아이디어 :
 - 버블 소트 문제로 아래와 같이 구현하면 바로 시간초과!
 - 해당 문제는 버블 정렬의 특성을 이용해서 해결책을 찾아야 하는 문제로 \
   정렬 전과 정렬 후의 인덱스 위치의 차이 중 가장 많은 차이를 보인 수가 버블정렬 횟수가 됨.

'''
'''
# 시간초과
import sys
from collections import defaultdict,Counter
input = sys.stdin.readline
       
N = int(input())        
A = [int(input()) for _ in range(N)]
for i in range(N):
    changed = False
    for j in range(N-i-1):            
        if A[j] > A[j+1]:
            changed = True
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
    
    if not changed:        
        print(i+1)
        break
'''
'''
# 딕셔너리를 사용하는 것이 시간초과를 방지하는 것으로 알았는데, 데이터가 많을 경우 그렇지 않은 것 같음
# 정렬한 뒤에 dictionary로 형변환, dictionary로 뺄샘하는 것도 형변환이 필요 하는 것이 시간초과 요소로 보임.
'''
import sys
# from collections import defaultdict
input = sys.stdin.readline
       
N = int(input())     
# data = defaultdict(int)
data = []
for i in range(N):
    data.append((int(input()),i))

result = (sorted(data, key=lambda x:x[0]))
# print(result)
ans = []
for i in range(N):
    ans.append(result[i][1] - data[i][1])
# print(ans)
print(max(ans)+1)