"""
https://school.programmers.co.kr/learn/courses/30/lessons/131128
문제 존1나 불친절하네 

1. x와 y 문자열 길이 긴 것을 기준으로 짝궁의 len만큼 for으로 같은 문자열들 배열에 개수만큼 추가 (중복 허용)
2. 짝궁이 존재하지않으면 -1 반환, 
   0으로만 구성되었으면 0 반환
3. count() 쓰면 줫댐 쓰면안댐 
"""

"""
def solution(X, Y):
    x=str(X)
    y=str(Y)

    partNum=[]

    for i in range(len(y)):
        if y[i] in x and y[i] not in partNum:
            cnt = min(x.count(y[i]), y.count(y[i]))
            for j in range(cnt): 
                partNum.append(y[i])

    if len(partNum) == 0:
        return -1

    if len(partNum) > 0 and len(partNum) == partNum.count('0'):
        return 0

    partNum.sort(reverse=True)

    return ''.join(partNum)
"""

from collections import Counter
"""
def solution(X, Y): # X, Y는 정수
    x=Counter(str(X))
    y=Counter(str(Y))

    arr=[] # 짝궁 수를 넣을 배열

    if len(x) > len(y): # x를 항상 길이가 짧은 변수로 선언
        x, y = y, x
 
    x_key=list(x.keys()) # x의 Counter형 key 리스트
    y_key=list(y.keys()) # y         "

    for i in range(len(x)): # 길이가 짧은 것을 기준으로 반복문
        if x_key[i] in y_key:
            
            print("i: ", i, "rng: ", rng)
            for _ in range(rng):
                arr.append(x_key[i])

    if len(arr)==0:
        return -1
    
    if len(arr) == arr.count('0'):
        return 0
    arr.sort(reverse=True)

    print("x: ", x)
    print("y: ", y)
    print("x_key: ", x_key)
    print("y_key: ", y_key)

    return "arr: ", ''.join(arr)
"""


from collections import Counter

def solution(X, Y):
    x=Counter(X)
    y=Counter(Y)
    
    answer=""
    
    if len(x) > len(y): # 항상 x가 짧은 길이
        x, y = y, x
        
    for i in x:
        rng=0
        if i in y:
            rng=min(x[i], y[i])
            
        for j in range(rng):
            answer += i # 서로가 가진 짝궁수에 맞게 추가
            
    if answer=="": # 짝궁 없
        return "-1"
    else:
        answer = sorted(answer, reverse=True)
        if answer[0] == '0':
            return "0"
    
    
    return ''.join(answer)

if __name__ == "__main__":
    X="11147911"
    Y="125790622"

    print(solution(X, Y))

