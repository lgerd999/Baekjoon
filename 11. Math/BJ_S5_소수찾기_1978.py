# https://www.acmicpc.net/problem/1978
# 소수 찾기 : 에라토스테네스의 체 알고리즘 적용
# 참조 : https://www.youtube.com/watch?v=9rLFFKmKzno&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=39
'''
알고리즘
1. 2부터 𝑁까지의 모든 자연수를 나열한다
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 𝑖를 찾는다
3. 남은 수 중에서 i의 배수를 모두 제거한다(𝑖는 제거하지 않는다)
4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다

'''
import sys
import math
input = sys.stdin.readline

# 에라토스테네스의 체 알고리즘
def prime_number(n):  #  2 ~ n 까지의 소수 구하기
    # 모든 수가 소수라고 가정하고 True로 값을 설정.(0과1은 제외)
    array = [True for i in range(n+1)]
    
    # 2부터 n의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(n)) +1):
        if array[i] == True:    # i가 소수인 경우
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i*j <= n:
                array[i*j] = 0
                j += 1
            '''
            # 아래와 같은 방식으로도 구할 수 있음.
            for j in range(i + i, n + 1, i):
                array[j] = False
            '''    
    return array        

N = int(input())
data = list(map(int,input().split()))

ans = prime_number(max(data))

cnt = 0
for i in data:
    if i == 1: continue
    if ans[i]:
        cnt += 1
print(cnt)        