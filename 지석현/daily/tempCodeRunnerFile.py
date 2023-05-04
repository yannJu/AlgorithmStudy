def solution(s):
    a=len(s)
    print("asd:", a*0.5%1)
    i=int(a*0.5)-1
    j=int(a*0.5)+1
    if a*0.5%1 == 0: # 짝수
        return s[i:j]
    else:
        return s[int(a*0.5)]


if __name__ == "__main__":
    X="abcede"
    print(solution(X))

