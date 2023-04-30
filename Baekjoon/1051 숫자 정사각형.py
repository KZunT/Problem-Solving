N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input())))

max_width = min(N, M)

answer = 0

for i in range(N):  # 모든 지점 탐색
    for j in range(M):
        for k in range(max_width):  # 지점마다 길이가 k 인 정사각형 조건을 만족하는 지 확인
            if (i + k) < N and (j + k) < M and (
                    board[i][j] == board[i + k][j] == board[i][j + k] == board[i + k][j + k]):
                answer = max(answer, (k + 1) * (k + 1))  # 구한 정사각형 넓이를 저장
print(answer)
