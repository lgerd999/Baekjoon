# https://www.acmicpc.net/problem/9935
#

import sys
input = sys.stdin.readline

S = input().rstrip()
E = input().rstrip()

E = list(E)
len_E = len(E)

index = 0

result = []

while index <= len(S)-1:
    result.append(S[index])
    index += 1
    
    if result[-len_E:] == E:
        result[-len_E:] = []

if result:
    print(''.join(result))
else:
    print("FRULA")            
        
