N = int(input())

d = []

for i in range(N):  # 값 입력받기
    d.append(list(map(int, input().split())))

for i in range(1, len(d)):  # 1부터 시작하는 이유는 첫번째 집은 RGB 중 아무거나 시작하는걸 가정으로 두기 때문
    # 각 R, G, B 로 첫번째 집이 시작하는 상황, 그 이후는 이전 집과 다른색중 값이 낮은걸 택하여 더해준다.
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + d[i][0]  # R
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + d[i][1]  # G
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + d[i][2]  # B

print(min(d[N - 1][0], d[N - 1][1], d[N - 1][2]))  # RGB 시작 케이스중 가장 낮은것을 출력
