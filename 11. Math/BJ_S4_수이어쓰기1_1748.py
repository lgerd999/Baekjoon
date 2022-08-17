# https://www.acmicpc.net/problem/1748
# 
import sys
input = sys.stdin.readline

N = input().rstrip()

'''
예를 들어, 120이라면 3자리이므로 1~9, 10 ~ 99 까지의 자리수를 미리 계산할 수 있다.
자리수 계산식은 다음과 같다.
table[i] = tablep[i-1] + 9 * 10**(i-1) *i, i = 1,...
'''
table = [0]*len(N)
for i in range(1,len(N)):
    table[i] = table[i-1] + 9 * 10**(i-1)*i

'''
예를 들어, 120이라면, 120-100= 20(101~120), 여기에 100까지 포함하면 21이됨.
21 * 자리수 + 1~99까지의 미리 계산된 값을 더하면 된다.
'''
ans = table[len(N)-1] + (int(N) - 10**(len(N)-1) +1)*len(N)
print(ans)
