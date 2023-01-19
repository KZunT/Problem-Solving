from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length, maxlen=bridge_length)
    truck_weights = deque(truck_weights)

    cur_weight = 0  # 현재 다리의 무게 (sum 함수 사용시 시간초과)

    while True:
        arrived_truck = bridge.popleft()
        cur_weight -= arrived_truck

        if len(truck_weights) == 0:
            answer += bridge_length
            break

        if cur_weight + truck_weights[0] <= weight:  # 다리에 트럭이 올라갈 수 있을때
            start_truck = truck_weights.popleft()
            bridge.append(start_truck)
            cur_weight += start_truck

        else:  # 못올라가면 대기
            bridge.append(0)

        answer += 1

    return answer

# def solution(bridge_length, weight, truck_weights):
#     q=[0]*bridge_length
#     sec=0
#     while q:
#         sec+=1
#         q.pop(0)
#         if truck_weights:
#             if sum(q)+truck_weights[0]<=weight:
#                 q.append(truck_weights.pop(0))
#             else:
#                 q.append(0)
#     return sec