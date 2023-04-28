def solution(bridge_length, weight, truck_weightss):
    time=0
    on_bridge=[0] * bridge_length # 다리 위의 트럭 
    on_bridge_weight = 0
    
    while len(truck_weights) or on_bridge_weight > 0: # 대기 중이거나 다리 위에 트럭이 없을 때까지
        passed=on_bridge.pop(0) # 다리 위 트럭 한 개 제거
        on_bridge_weight-=passed # 제거한 트럭 무게도 같이 빼주고

        if len(truck_weights) and truck_weights[0] + on_bridge_weight <= weight:
            on_bridge_weight+=truck_weights[0]
            t = truck_weights.pop(0) # 대기열에 있는 트럭 뺴서
            on_bridge.append(t) # 다리 위에 위치

        else:
            on_bridge.append(0) # 다리 과부하 -> 다음 턴
                
        time+=1 # 한 턴

    return time

if __name__=="__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]

    print(solution(bridge_length, weight, truck_weights))

    





     





# if __name__ == "__main__":
#     s=121
#     print(solution(s))
