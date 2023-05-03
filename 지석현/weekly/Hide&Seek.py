"""
https://www.acmicpc.net/problem/1697

1.수빈이의 위치 점 N(0 ≤ N ≤ 100,000),  동생의 위치 점 K(0 ≤ K ≤ 100,000)
2.수빈이는 걷거나 순간이동 가능
    - 걷기: 1초 후 (X-1) 또는 (X+1)
    - 텔포: 1초 후 X*2
3. 수빈이가 동생을 찾을 수 있는 가장 빠른 시간은 몇 초후인가? 찾으면 뒤진다
ㅡㅡㅡㅡㅡㅡㅡNㅡㅡㅡ.......ㅡㅡㅡㅡKㅡㅡㅡㅡ.....
0                     ~                    100,000
"""

from collections import deque
def solution(n, k):
    # 큐 및 방문 리스트
    q = []
    v = [0] * 200001

    q.append(n) # 수비닝 위치(시작 위치)
    v[n] = 1 # 시작 위치 방문 리스트에 추가

    while q:
        c = q.pop(0) # 현재 위치

        if c == k: # 찾은 경우
            return v[k]-1
        
        for i in (c-1, c+1, c*2):
            if 0 <= i <= 200000 and v[i] == 0: # 범위 내이고 방문한 적 없다면
                q.append(i)
                v[i] = v[c]+1 # 한 층 더 내려감
    



    


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solution(n, k))