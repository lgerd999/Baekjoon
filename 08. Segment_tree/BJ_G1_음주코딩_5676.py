# https://www.acmicpc.net/problem/5676
# 세그먼트 트리
'''
구간곱하기 문제와 유사
https://www.acmicpc.net/problem/11505

위의 문제와 동일하게 코드를 넣게 되면 시간초과에 걸리게 된다.
문제에서 답은 음수,양수,0만 판별하면 되기 때문에 곱셈의 양을 줄여주는 쪽으로 구현하면 시간초과를 해결할 수 있다.

'''
import sys
from math import ceil,log2
input = sys.stdin.readline

def detect_sign(num):
    if num > 0:
        return 1
    elif num == 0:
        return 0
    else:
        return -1        

# 초기화
def init(node,start,end):
    # 리트 노드인 경우
    if start == end:
        tree[node] = detect_sign(S[start])
    # 구간 곱    
    else:    
        init(node*2,start,(start+end)//2)
        init(node*2 + 1,(start+end)//2 +1,end)
        tree[node] = tree[node*2] * tree[node*2 +1]    
    

def query(node,start,end,left,right):
    if end < left or start > right:
        return 1
    if start >= left and end <= right:
        return tree[node]
    else:    
        return query(2*node,start,(start+end)//2,left,right) * query(2*node + 1,(start+end)//2 + 1,end,left,right)
        
def update(node,start,end,idx,val):
    if start > idx or end < idx:
        return        
    if start == end:
        S[idx] = val
        tree[node] = detect_sign(val)
        return
    update(node*2, start, (start+end)//2, idx, val)
    update(node*2 +1 , (start+end)//2 +1, end, idx, val)
    tree[node] = tree[node*2] * tree[node*2 +1]

while True:
    try:
        # N : 수열의 크기, K : 게임의 라운드 수
        N,K = map(int,input().split())        
        S = list(map(int,input().split()))
        # print('S=', S)
        h = ceil(log2(N))
        tree_size = 1 << (h+1)
        tree = [0] * tree_size

        init(1,0,N-1)
        ans = ''
        for i in range(K):
            cmd, a, b = map(str,input().split())
            # cmd가 C인경우, a번째 수를 b로 변경
            # cmd가 P인경우, a번째 수부터 b번째 수까지 곱을 구함
            a,b = int(a),int(b)
            if cmd == 'C':
                update(1,0,N-1,(a-1),(b))
            elif cmd == 'P':
                # a에서 b까지 구간 곱
                value = query(1,0,N-1,a-1,b-1)
                if value > 0:
                    ans += '+'
                elif value == 0:
                    ans += '0'
                else:
                    ans += '-'
        print(''.join(map(str,ans)))                  
    except Exception:
        break
