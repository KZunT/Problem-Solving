T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    planet = 0  # 행성

    for _ in range(N):
        dx, dy, r = map(int, input().split())
        start = (((x1 - dx) ** 2) + ((y1 - dy) ** 2)) ** 0.5  # 시작점까지의 거리
        end = (((dx - x2) ** 2) + ((dy - y2) ** 2)) ** 0.5  # 도착점까지의 거리

        if start < r and end < r:  # 시작점과 도착점 모두 원 안에 있을 경우
            pass
        elif start < r:  # 시작점이 안에 있을 경우
            planet += 1
        elif end < r:  # 도착점이 안에 있을 경우
            planet += 1

    print(planet)
