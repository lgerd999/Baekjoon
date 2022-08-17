# https://www.acmicpc.net/problem/1790
# 이분 탐색
import sys
input = sys.stdin.readline
'''
아이디어
1. 1부터 N까지 숫자를 이어붙였을때 길이를 구한다. 그리고, 그 길이보다 K가 작다면 이분탐색으로 다시 N값을 찾는다.
2. mid 값을 구해서 1부터 mid까지 숫자를 이어붙여본다. 그 값이 K보다 작다면 mid를 더 증가시킨다.
3. 예를 들어, N = 20, K=23이라면, mid = (1+20)//2 = 10, 1부터 10까지 붙인 길이 < K라면,
    이전 mid 값은 start값이 되어 mid = (10+20)//2 = 15, 1부터 15까지 붙인 길이 < K라면,
    mid = (15+20)//2 = 17, 1부터 17까지 붙인 길이 > K이므로, mid 값은 end가 된다.
    mid = (15+17)// = 16
4. 위치를 찾았으면 자리수 고려해서 값을 찾는다.
'''
'''
예를 들어, 120이라면 3자리이므로 1~9, 10 ~ 99 까지의 자리수를 미리 계산할 수 있다.
자리수 계산식은 다음과 같다.
table[i] = tablep[i-1] + 9 * 10**(i-1) *i, i = 1,...
'''
'''
예를 들어, 120이라면, 120-100= 20(101~120), 여기에 100까지 포함하면 21이됨.
21 * 자리수 + 1~99까지의 미리 계산된 값을 더하면 된다.
ans = table[len(N)-1] + (int(N) - 10**(len(N)-1) +1)*len(N)
'''

def numb_digit(n):
    return table[len(n)-1] + (int(n) - 10**(len(n)-1) +1)*len(n)

N,k = map(str,input().split())

# 테이블 생성시 기준점을 N,k에 두면 index error 또는 답이 틀릴 수 있음. 문제에서 k는 1,000,000,000 범위까지 가지니 최고 10자리를 고려.
table = [0]*10
for i in range(1,10):
    table[i] = table[i-1] + 9 * 10**(i-1)*i

if numb_digit(N) < int(k):
    print(-1)
else:    
    start = 0
    end = int(N)    
    ans = 0    
    while start <= end: 
        mid = (start + end)//2
        total = numb_digit(str(mid))
        if total < int(k):            
            start = mid+1
        else:      
            ans = mid              
            end = mid-1
    # 자리수 계산 : k - (1부터 ans까지 숫자를 이어붙인 자리수)
    len = int(k)-numb_digit(str(ans))    
    print(str(ans)[len-1])         
    
