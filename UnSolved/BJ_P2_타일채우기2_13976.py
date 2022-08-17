# https://www.acmicpc.net/problem/13976
# 유사 문제 : https://www.acmicpc.net/problem/2133
# 참조 : https://blog.naver.com/PostView.nhn?blogId=mym0404&logNo=222221902314&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView
'''
3xN 크기의 벽을 2x1, 1x2 크기의 타일로 채우는 경우의 수 구하기
단, 2133번 문제와 다른점은 N이 1,000,000,000,000,000,000까지 입력되므로
메모리 제한(512MB)내에서 이를 해결해야 함

* 수식 간소화 : 
F(n) = 3*F(n-2) + 2{F(n-4) + F(n-6) + F(n-8) +........+ F(0)}
-> 이 식에서 n 대신 n-2를 대입
F(n-2) = 3*F(n-4) + 2{F(n-6) + F(n-8) + F(n-10) +........+ F(0)}
-> 두 식을 빼면
F(n)-F(n-2) = 3*F(n-2) - F(n-4)

정리하면,
 F(n) = 4*F(n-2) - F(n-4)

 이를 행렬로 변환?

'''

N = int(input())
DP = [0]*(N+1)
DP[0:2] = [1,0,3]
# summ = 0
# for i in range(2,N+1,2):
#     summ += DP[i-4]
#     DP[i] = (3* DP[i-2] + 2*summ)%1000000007    
# print(DP[N])

for i in range(4,N+1,2):
    DP[i] = (4*DP[i-2] - DP[i-4])%1000000007  
print(DP[N])    