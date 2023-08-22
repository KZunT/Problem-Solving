N = int(input())
candy = [list(input()) for _ in range(N)]

answer = 0


def check_col():
    global answer

    for i in range(N):
        length = 1
        for j in range(N - 1):
            if candy[i][j] == candy[i][j + 1]:
                length += 1
                answer = max(answer, length)
            else:
                length = 1


def check_row():
    global answer

    for i in range(N):
        length = 1
        for j in range(N - 1):
            if candy[j][i] == candy[j + 1][i]:
                length += 1
                answer = max(answer, length)
            else:
                length = 1


for i in range(N):
    for j in range(N - 1):
        # 열 변경
        if candy[i][j] != candy[i][j + 1]:
            # swap
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            check_col()
            check_row()
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
        # 행 변경
        if candy[j][i] != candy[j + 1][i]:
            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]
            check_col()
            check_row()
            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]

print(answer)
