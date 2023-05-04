""" 
1.각 기사단의 번호에 맞는 약수 개수 구하기
2.약수의 개수가 limit보다 크면 power로 대신함
3. 배열 합 리턴
"""

number=10
limit=3
power=2
kg=1 # number1 계산에서 빼버리기

# 약수의 개수 구하기
def count(n, limit, power):
    if (n**0.5)%1==0: 
        cnt=3 # 1과 자기자신과 제곱근 제외
        rng=int(n**0.5)
    else:
        cnt=2 # 1과 자기자신 제외
        rng=int(n**0.5+1)

    for i in range(2, rng):
        if n%i==0: # 약수면
            cnt+=2
        if cnt>limit:
            return power


    return cnt

for i in range(2, number+1): # number2 ~ numberN 
    # 공격력=무게
    asd=count(i, limit, power)
    kg+=asd

print(kg)