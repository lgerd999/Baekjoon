#
#
'''
이항 계수 = nCk = n!/k!(n-k)! = n x (n-1) x ... (n-k+1)/k!

'''

def factorial(n):
    mul = 1    
    for i in range(1,n+1):
        mul *= i        
    return mul  

N,K = map(int,input().split())
c = factorial(N)//(factorial(K)*factorial(N-K))
print(c)
