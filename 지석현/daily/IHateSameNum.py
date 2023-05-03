"""
https://school.programmers.co.kr/learn/courses/30/lessons/12906

"""

from collections import Counter
def solution(arr):
    answer=[arr[0]]
    for i in arr:
        if answer[-1] == i:
            continue
        else:
            answer.append(i)

    return answer


if __name__ == "__main__":
    arr=[1,1,3,3,0,1,1]

    print(solution(arr))
