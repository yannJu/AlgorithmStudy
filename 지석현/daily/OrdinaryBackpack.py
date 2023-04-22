# https://www.acmicpc.net/problem/12865
#
# 문제: 평범한 배낭
#   - 들고갈 물건 후보들 N개 중, 각 물건의 무게(W)와 가치(V)의 여러 경우의 수를 판별
#   - 제한된 무게(K)이하인 물건(들)의 최대 가치 구하기
# 
# 관련 알고리즘 : 냅색(Knapsack) 알고리즘_0-1 Knapsack


# n, k = map(int, input().split())

# stuff = [[0,0]]
# DP = [[0] * (k+1) for _ in range(n+1)]

# for _ in range(n):
#     stuff.append(list(map(int, input().split())))

# for i in range(1,n+1):
#     for j in range(1,k+1):
#         w,v = stuff[i]
#         if j >= w:
#             DP[i][j] = max(DP[i-1][j] , DP[i-1][j-w] + v)
#         else:
#             DP[i][j] = DP[i-1][j]

# print(DP[i][k])


n, k = map(int,input().split()) # 물건 개수(n)와 들 수 있는 최대 무게(k)
items = [[0, 0]]  # 물건 번호와 가치 저장 리스트
dp = [[0 for _ in range(k+1)] for _ in range(n+1)] # 경우의 수 리스트

for i in range(n): # 물건의 개수만큼 무게와 가중치 각각 입력 받기
     items.append(list(map(int, input().split())))

# 냅색 알고리즘
for i in range(1, n+1):
    w, v = items[i]
    for j in range(1, k+1):
        

        if j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])



