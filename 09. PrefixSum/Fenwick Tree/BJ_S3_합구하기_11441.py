# https://www.acmicpc.net/problem/11441
# Fenwick Tree
'''
Fenwick Tree(BIT)
- 합을 구하는 경우 세그먼트 트리의 오른쪽 자식은 필요 없다.
- L(i) : i를 2진수로 나타냈을 때 가장 마지막이 1이 나타내는 값
   3 = 11   ==> 1의 위치 0 : 2^0, L(3) = 1
   9 = 1001 ==> 1의 위치 0 : 2^0 = 1, L(9) = 1
   16 = 10000 ==> 1의 위치 4 : 2^4 = 16, L(16) = 16
   ==> L(i) = num & -num
- Tree[i]의 의미 : i까지 L(i)개의 합
 예) Tree[12] = L(12):4 => 4개의 합 : A[9]+A[10]+A[11]+A[12]
- Fenwick Tree는 구간의 합을 구할 수 없다. 첫 번째 수부터 i번째수까지 합만 구할 수 있다.
- query함수 구현
 A[1]+...+A[13]까지의 합을 구한다면, 
 13 = 1101, L(13)=2^0=1, tree[13] = A[13]
 12 = 1100, L(12)=2^2=4, tree[12] = A[9]+A[10]+A[11]+A[12]
 8 = 1000,  L(8)=2^3=8,  tree[8] = A[1]+...A[8]
 ==> 이진수의 길이만큼의 시간이 필요하므로 O(logN)
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

def query(i):
    ans = 0
    while i > 0 :
        ans += tree[i]
        i -= i & -i 
    return ans        

def update(i,num):
    while i <= N:
        tree[i] += num
        i += (i & -i)

N = int(input())
array = list(map(int,input().split()))
tree = defaultdict(int)

for i in range(N):
    update(i+1,array[i])

print(tree)

M = int(input())
for _ in range(M):
    i,j = map(int,input().split())
    ans = query(j) - query(i-1)   
    print(ans)
    