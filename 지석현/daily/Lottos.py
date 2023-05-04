# https://school.programmers.co.kr/learn/courses/30/lessons/77484?language=python3
# 로또의 최고 순위와 최저 순위

# 1. 내 번호 중 "0" 카운트 zero_count
# 2. 0을 제외한 번호 중 당첨 번호와 같은 번호 카운트 count
# 3. 내 번호 중 당첨 번호의 개수 = min
# 4. 내 번호 중 당첨 번호의 개수 + 0의 모든 개수 = max
# 5. 생각해야할 것: count와 zero_count가 0일때 순위 표현 방법


""" 처음 코딩한 것
1. 너무 난잡하다
2. min, max 값을 좀 더 간단하게 표현가능할 것 같은데, 무식한 방법으로 처리한 느낌
def solution(lottos, win_nums):
    answer = []
    
    count = 0 # 정답 개수 
    zero_count = lottos.count(0)  # 0의 개수

    for i in range(len(win_nums)):            
        if win_nums[i] in lottos:
            count+=1

    min = 7 - count
    max = min - zero_count

    if min == 7:
        min = 6
    if max == 7:
        max = 6

    print(zero_count)

    answer.append(min)
    answer.append(max)

    return answer
"""

# if __name__ == "__main__":
#     lottos = [0, 0, 3, 4, 5, 6]
#     win_nums = [7, 8, 9, 10, 11, 12] 
#     solution(lottos, win_nums)