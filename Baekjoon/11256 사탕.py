T = int(input())

for _ in range(T):
    J, N = map(int, input().split())
    boxes = []
    for _ in range(N):
        R, C = map(int, input().split())  # 세로, 가로
        boxes.append(R * C)
    boxes.sort(reverse=True)

    cnt = 0
    
    while J > 0:
        J -= boxes[cnt]
        cnt += 1

    print(cnt)
