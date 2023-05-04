"""
https://school.programmers.co.kr/learn/courses/30/lessons/12901
"""
def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    weeks = ['FRI',"SAT",'SUN','MON',"TUE",'WED','THU'] * 2
    temp=0
    #2016년 1월 1일은 FRI 3 28 목
    #       2월 1일은 MON 1 2 TUE
    #       3월 1일은 TUE 3
    #       4월 1일은 FRI 2
    #       5월 1일은 SUN 3
    #       5월 24일은 TUE
    #       weeks[temp+((b-1)%7)]

    if a == 1: # 1월인 경우
        return weeks[b%7-1]
    else: # 1월이 아닌경우
        for i in range(a-1):
            temp+=days[i] # 각 달의 1일의 요일
        
        temp+=b # 이전 월의 모든일 + b
        
        return weeks[temp%7-1] # 최종 요일

if __name__ == "__main__":
    a=5
    b=24
    print(solution(a, b))