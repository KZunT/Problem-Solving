img = [[0] * 100 for _ in range(100 + 1)]

cnt = 0

for _ in range(4):
    xmin, ymin, xmax, ymax = map(int, input().split())  # 왼쪽 아래 좌표, 오른쪽 위 좌표

    for i in range(xmin, xmax):
        for j in range(ymin, ymax):
            if img[i][j] == 0:
                img[i][j] += 1  # 박스를 칠한 면적을 구하기
                cnt += 1

print(cnt)
