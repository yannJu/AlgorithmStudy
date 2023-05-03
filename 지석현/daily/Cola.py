"""
1. 콜라 빈 병2개를 가져다주면 새 콜라 1병을 주는 마트가 있다. 
2. 이로 인해, 만약 20병의 새 콜라가 있다면 총 19병의 콜라를 받을 수 있다.
3. 빈 병 a개를 가져다주면 새 콜라b개를 주는 마트가 있다면, n개의 새 콜라를 통해 받을 수
    있는 새 콜라의 개수는?
"""


def solution(a, b, n):
    answer = 0

    x=n  # 새 콜라
    y=0  # 새 콜라로 바꾸기전 남은 새 콜라 
    m=0  # 한 턴에서 빈 병을 새 콜라로 바꾼 수

    while x>=a:
        m, y=(x//a)*b, (x%a)
        print(m, y)
        answer+=m
        x=m+y

    return answer


if __name__ == "__main__":
    a=3
    b=1
    n=20

    print(solution(a, b, n))