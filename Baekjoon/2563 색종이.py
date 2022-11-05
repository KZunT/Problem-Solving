paper = [[0] * 101 for i in range(101)]  # 흰 종이 영역

for _ in range(int(input())):
    x, y = map(int, input().split())

    for i in range(10):  # 검은색이 있는 부분을 1로 채움
        for j in range(10):
            paper[x + i][y + j] = 1

area = 0

for i in paper:  # 1로 채워진 영역 합산
    area += sum(i)

print(area)
