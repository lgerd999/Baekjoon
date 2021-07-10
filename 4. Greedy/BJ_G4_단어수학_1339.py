# https://www.acmicpc.net/problem/1339

from collections import defaultdict
'''
구현 아이디어
1. 딕셔너리 Key에 문자, Value에 값을 저장
2. 십진수 덧셈 적용
   - GCF : 100xG + 10xC + F --> pow 함수 이용
   - ACDEB : 10000xA + 1000xC + 100xD + 10x E + B
   - GCF + ACDEB = F + B + 10xE + 100xG + 100xD + 1010xC + 10000xA
   - 딕셔너리 적용하면,
    {'F': 1, 'B': 1, 'E': 10, 'G': 100, 'D': 100, 'C': 1010, 'A': 10000}
3. 9 - 각 행 자리수 부터 9까지 곱하면 답
'''
N = int(input())
data = [list(map(str,input().rstrip())) for _ in range(N)]
table = defaultdict(int)
for i in range(N):    
    for j in range(len(data[i])):                
        table[data[i][j]] += pow(10,len(data[i])-1-j)               
A = dict(sorted(table.items(),key=lambda x:x[1]))
ans = 0
for i,j in enumerate(A.values(),10-len(A.values())): # 9 - 각행 길이 + 1
    ans += i * j
print(ans)    
