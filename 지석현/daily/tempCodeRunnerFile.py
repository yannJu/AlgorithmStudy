###### 테스트용 파일 ######

n=10

if (n**0.5)%1==0: 
    cnt=3 # 1과 자기자신과 제곱근 제외
    for i in range(2, int(n**0.5)):
        if n%i==0: # 약수면
            cnt+=2
else:
    cnt=2 # 1과 자기자신 제외
    for i in range(2, int(n**0.5)+1):
        if n%i==0: # 약수면
            cnt+=2

print(cnt)