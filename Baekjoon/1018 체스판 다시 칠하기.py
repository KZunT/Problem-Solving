N, M = map(int, input().split())
# 이게 브루트포스??..

board = []
result = []

for _ in range(N):
    board.append(input())  # 체스판 입력받기

for i in range(N - 7):
    for j in range(M - 7):  # 시작 좌표
        # b,w 로 시작하는 상황을 동시에 계산
        start_black = 0
        start_white = 0

        for a in range(i, i + 8):  # 시작 좌표로 부터 8x8 을 탐색한다.
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:  # 현재 좌표를 기준으로 다른 붙어있는 좌표와 색이 다른지 비교, 좌표 합이 짝수이면 시작점과 같은색임
                    if board[a][b] != 'B':
                        start_black += 1
                    if board[a][b] != 'W':
                        start_white += 1
                else:  # 좌표의 합이 홀수이면 시작점과 다른색이다.
                    if board[a][b] != 'W':
                        start_black += 1
                    if board[a][b] != 'B':
                        start_white += 1

        result.append(start_black)
        result.append(start_white)

print(min(result))
