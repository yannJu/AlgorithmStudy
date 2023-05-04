"""
https://school.programmers.co.kr/learn/courses/30/lessons/12926

문제 요약------------------------
1. 일정 거리만큼 밀어서 다른 알파벳과 대칭인 관계
2. "z"는 1만큼 밀면 "a"가 됨 -> lower[25↑] 이면 다시 0으로
3. 공백은 밀어도 공백
4. 문자열 s <= 8000
   밀 거리 1 <= n <= 25 
풀이 ------------------------------
1. s[i]가 lower or upper인지 판별
2. lower or upper의 index번호 몇번인지 확인
3. 판별한 인덱스 번호 +n을 answer에 추가

"""
def solution(s, n):
    answer=[]

    lower="abcdefghijklmnopqrstuvwxyz"*2
    upper=lower.upper()


    for i in range(len(s)):
        if s[i]==" ":
            answer.append(" ")
        elif s[i].isupper():
            answer.append(upper[upper.index(s[i])+n])
        else: 
            answer.append(lower[lower.index(s[i])+n])
    
    return ''.join(answer)

if __name__ == "__main__":
    s="A B"
    n=1

    print(solution(s, n))