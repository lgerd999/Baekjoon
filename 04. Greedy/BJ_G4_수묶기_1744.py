# https://www.acmicpc.net/problem/1744
#
'''
수열의 합을 구하는 문제인데 수열의 두 수를 묶어 곱해서 합이 최대가 되게 하는 값을 찾는 문제

구현
1. 수를 오름차순으로 정렬한다.
2. 양수와 음수,0과 1로 분리한다.
3. 수열의 길이를 고려하여 2개 묶음으로 잘라서 묶은 수를 곱해고 전체는 더한다.
  - 0과 양수 = 덧셈
  - 0과 음수 = 곱셈
  - 1이 포함되면 덧셈(1과 양수 = 덧셈, 1과 음수 = 덧셈)
  - 양수,양수 = 곱셈
  - 음수,음수 = 곱셈
  - 양수,음수 = 덧셈
  - 리스트 길이가 홀수 일 때 정렬시 양수와 음수가 묶였을 때 최대값이 아닐 수 있는 경우 고려
    -- 양수를 더하고 음수를 다음 음수와 곱한다.
    -- 음수를 더하고 양수를 다음 양수와 곱한다.

'''
import sys
from collections import defaultdict
input = sys.stdin.readline

'''
# 반례는 모두 찾아서 맞춰봤지만, 결과는 틀렸다고 나온다.
# 아래 코드는 예외 처리가 너무 복잡해서 재구현으로 가닥을 잡았다.
def number_bind(numbers):
    conn = []
    ans = 0
    for i in range(N):
        conn.append(numbers[i])
        # 잔여 길이, 두 수의 부호, 0 과 1
        # 리스트 길이가 짝수
        remain = len(numbers[i:])
        # print(len(numbers[:i]),remain)
        if len(conn)%2 == 0 :
            # 두 수 중 하나가 0인 경우
            if conn[0] * conn[1] == 0:
                # 0 이 연속으로 들어오는 경우를 고려하여 conn[0 or 1] == 0 인 경우도 추가.
                if not conn[1] and conn[0] >= 0: # 0과 양수, 0과 0
                    mul = conn.pop(0)
                elif not conn[0] and conn[1] > 0: # 0과 양수   
                    mul = conn.pop()
                else:                   # 0과 음수
                    mul = conn.pop() * conn.pop()  
            # 두 수 중 하나가 1인 경우
            elif conn[0] == 1:  # 1 포함
                mul = conn.pop(0)
            elif conn[1] == 1:  # 1 포함
                mul = conn.pop()      
            # 양수,양수 또는 음수,음수인 경우          
            elif conn[0]*conn[1] > 1:                
                mul = conn.pop() * conn.pop()   # 양수, 양수 및 음수, 음수    
            else:     
                # 양수, 음수인 경우에서 잔여 리스트가 남아 있는 경우는 양수를 더하고, 음수는 뒷자리와 묶는다.              
                if remain:
                    if conn[0] > 1:
                        mul = conn.pop(0)
                    elif conn[1] > 1:
                        mul = conn.pop()
                else:       
                    mul = conn.pop() + conn.pop()   # 양수, 음수
            ans += mul    
    if conn:        
        ans += conn[-1]
    # print(ans)    
    return ans    

N = int(input())
num = [int(input().rstrip()) for _ in range(N)]

# 내림 차순 정렬
num_asc = sorted(num,reverse=True)
num_dsc = sorted(num)
# print(num_asc)
# print(num_dsc)

result = max(number_bind(num_asc),number_bind(num_dsc))
print(result)     
'''
N = int(input())
num = [int(input().rstrip()) for _ in range(N)]       

# 음수, 양수, 1로 구분하여 입력을 받는다.
# 
numbers = defaultdict(list)

for i in num:
    if i <= 0:   # 0과 음수, 오름차순
        numbers[0].append(i)
        numbers[0].sort()
    elif i == 1 :
        numbers[1].append(i)
    elif i > 1: # # 양수, 내림차순
        numbers[2].append(i)
        numbers[2].sort(reverse=True)
     
# print(numbers)

ans = 0
for i in range(3):
    oper = len(numbers[i])
    if not oper: continue

    conn = []
    for j in range(oper):
        conn.append(numbers[i][j])
        if len(conn)%2 == 0:
            match i:
                case 0: # 음수
                    ans += conn.pop()*conn.pop()
                case 2: # 양수            
                    ans += conn.pop()*conn.pop()
                case 1: # 1
                    ans += conn.pop()+conn.pop()
    if conn:
        ans += conn[-1]
            
print(ans)


'''
반례)
0이 연속으로 2개 
5
-5
-2
-3
0
0
-----
15

수열이 모두 음수
5
-1
-2
-3
-4
-5
-----
25

1일 곱할 것이냐 더할 것이냐
6
5
4
3
1
1
1
-----
26


6
-5
-2
-1
0
3
6
-----
28

-5와 1일 때 즉, 1과 음수일때 처리(덧셈)
13
-10
-9
-8
-7
-6
-5
1
2
3
4
5
6
7
-----
245

순서대로 자르는게 답이 아닐 수 있는 반례
내림 [257, 157, 81, -435, -537]
올림 [-537, -435, 81, 157, 257]
5
-537
81
-435
257
157
-----
274025
'''