# https://www.acmicpc.net/problem/12865
#
# 문제: 평범한 배낭
#   - 들고갈 물건 후보들 N개 중, 각 물건의 무게(W)와 가치(V)의 여러 경우의 수를 판별
#   - 제한된 무게(K)이하인 물건(들)의 최대 가치 구하기
# 
# 관련 알고리즘 : 냅색(Knapsack) 알고리즘
#                   - Fraction Knapsack: 나눌 수 있는 물건에 문제 즉, 무게 대비 가치를 구해 해결 -> greedy 
#                   - 0-1 Knapsack: 나눌 수 없는 물건에 대한 문제 -> 이번 문제에 적용할 알고리즘

n, k = map(int,input().split()) # 물건 개수(n)와 들 수 있는 최대 무게(k)
items = [[0, 0]]  # 물건 번호와 가치 저장 리스트
dp = [[0 for _ in range(k+1)] for _ in range(n+1)] # (가방 최대 무게+1) * (물건 개수+1) 리스트 생성


# 물건의 개수만큼 무게와 가중치 각각 리스트 형식으로 입력 받아 넣기
for i in range(n): 
    items.append(list(map(int, input().split())))

# 냅색 알고리즘
for i in range(1, n+1):
    w, v = items[i] # items[i][]
    for j in range(1, k+1):
        # 공간이 있을 때
        if j >= w:
            # 배낭 최대 용량 j 일 때, i번째 물건을 넣을려는 상황 = 이전 가치값 vs i번째 물건 넣었을 때 가치값
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v) 

        # 공간이 없으면 그냥 이전 값 고대로 계승
        else: 
            # 배낭 최대 용량 j 일 때, i-1번째 물건까지 확인한 최대 가치값
            dp[i][j] = dp[i-1][j] 

# k: 마지막까지 왔을 때의 값 = 최대 가치 값
print(dp[n][k]) 


# 살펴보면 좋은 사이트
# https://chanhuiseok.github.io/posts/improve-6/ - 냅색 알고리즘 기반 2차원 배열 풀이 + 1차원 배열 풀이