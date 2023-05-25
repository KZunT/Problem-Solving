N, W, L = map(int, input().split())  # 트럭 수, 다리 길이, 최대 하중
truck = list(map(int, input().split()))

bridge = [0] * W
time = 0

while bridge:  # 모든 트럭이 지나갈 때 까지 수행
    time += 1
    bridge.pop(0)
    if truck:
        if sum(bridge) + truck[0] <= L:  # 하중 초과 안하는 경우
            bridge.append(truck.pop(0))
        else:  # 하중 초과를 하면 잠시 멈춤
            bridge.append(0)

print(time)