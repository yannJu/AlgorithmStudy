"""
https://school.programmers.co.kr/learn/courses/30/lessons/81301

1. for문에서 1씩 증가시키며 숫자인지 확인(딕셔너리 벨류)
2. 숫자라면 패스
3. 숫자가아니라면 중첩
4. 중첩된 문자를 키와 비교
5. 중첩된 문자를 키로 변환
6. 반복.
"""

def solution(s):
    temp=""
    answer=""
    
    numEng={'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

    for i in range(len(s)):
        if s[i] in numEng.values(): # 숫자라면 answer에 추가
            answer+=s[i]
            print(s[i], "추가")
        else: # 문자라면 
            temp+=s[i]
            print("temp: ", temp)
            if temp in numEng:
                answer+=numEng[temp]
                temp=""

    return answer

if __name__ == "__main__":
    X="23four5six7"
    print(solution(X))