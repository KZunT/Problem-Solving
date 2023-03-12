# pypy3 사용
# import sys
# N = int(sys.stdin.readline().rstrip())
# answer = 0
# queen = [0] * N
#
# def check(x):
#     for i in range(x):
#         if queen[x] == queen[i] or abs(queen[x] - queen[i]) == abs(x - i):
#             return False
#     return True
#
#
# def n_queens(x):
#     global answer
#
#     if x == N:
#         answer += 1
#
#     else:
#         for i in range(N):
#             # [x, i]에 퀸을 놓겠다.
#             queen[x] = i
#             if check(x):
#                 n_queens(x + 1)
#
# n_queens(0)
# print(answer)

def dfs(queen, n, row):
    count = 0

    if n == row:
        return 1

    # 가로로 한번만 진행
    for col in range(n):
        queen[row] = col

        # for-else구문
        for x in range(row):
            # 세로로 겹치면 안됨
            if queen[x] == queen[row]:
                break

            # 대각선으로 겹치면 안됨
            if abs(queen[x] - queen[row]) == (row - x):
                break
        else:
            count += dfs(queen, n, row + 1)

    return count


N = int(input())

queen = [0] * N
print(dfs(queen, N, 0))