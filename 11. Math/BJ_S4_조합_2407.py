# https://www.acmicpc.net/problem/2407
#
'''
조합 공식 
nCr = n!/ r!(n-r)!
'''
def factorial(n):
    mul = 1    
    for i in range(1,n+1):
        mul *= i        
    return mul  

N,K = map(int,input().split())
c = factorial(N)//(factorial(K)*factorial(N-K))
print(c)

