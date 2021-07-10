# https://www.acmicpc.net/problem/11729
# 
'''
옮기려는 원반의 개수 n
옮길 원반이 현재 있는 출발점 기둥 from
원반이 도착할 기둥 to
옮기는 과정에서 사용될 보조 기둥 aux


'''
def hanoi(n,from_,to_,aux_):        
    if n == 1:  # 원반 1개        
        result.append([from_,to_])
        #print('N=1,',from_,to_)
        return
    # 원반 n-1개를 보조기둥(aux)로 이동
    hanoi(n-1,from_,aux_,to_)    
    # 가장 큰 원반을 목적지로 이동
    #print(n,from_,to_)    
    result.append([from_,to_])
    # aux에 있는 원반 n-1개를 목적지로 이동
    hanoi(n-1,aux_,to_,from_)

result = []
N = int(input())
# 원반 N를 기둥1번에서 3번으로 이동하며 기둥 2번은 보조 기둥으로 활용
hanoi(N,1,3,2)
ans = len(result)
print(ans)
for i in range(ans):
    print(*result[i], end=' ')
    print()

