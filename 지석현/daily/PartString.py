"""
https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=python3
"""

def solution(t, p):
    answer=0
    for i in range(len(t)-len(p)+1):
        if t[i:i+len(p)] <= p:
            answer+=1
    return answer


if __name__ == "__main__":
    t="500220839878"
    p="7"
    print(solution(t, p))