# 큐 - 카드 건네기

import collections as queue

# def conv_rotate(l,n):
#     return l[n:] + l[:n]

#N = int(input())    
N = 6 #3 5 4 2 1 
card = queue.deque(int(x) for x in range(1,N+1))

# 여기서부터 작성

for i in range(N-1):    
    x = card.popleft() 
    card.rotate(-1)

print(*card)

 



