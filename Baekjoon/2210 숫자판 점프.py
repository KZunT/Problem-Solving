def dfs(x, y, number):
    if len(number) == 6:  # 6자리 숫자가 만들어졌다면
        if number not in result:
            result.append(number)
        return

    dx = [1, -1, 0, 0]  # 상하좌우 확인 x
    dy = [0, 0, 1, -1]  # 상하좌우 확인 y

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:  # 범위 내에 있다면
            dfs(nx, ny, number + matrix[nx][ny])


# 입력
matrix = [list(map(str, input().split())) for _ in range(5)]

result = []

for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j])  # 모든 좌표 체크

print(len(result))