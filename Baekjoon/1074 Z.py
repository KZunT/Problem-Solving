# import sys
#
# N, r, c = map(int, input().split())
#
# N = 2 ** N
#
# Z_list = [[0 for _ in range(N)] for _ in range(N)]
#
# cnt = 0
#
#
# def divncon(start, end, n):
#     global cnt
#
#     if start > r or start + n <= r or end > c or end + n <= c:  # 범위 내에 찾는 값이 없다면 해당 변을 모두 탐색한 값을 더해줌
#         cnt += n ** 2
#         return
#
#     if n > 2:
#         n = n // 2
#         divncon(start, end, n)
#         divncon(start, end + n, n)
#         divncon(start + n, end, n)
#         divncon(start + n, end + n, n)
#     else:  # n 이 1
#         if start == r and end == c:
#             print(cnt)
#         elif start == r and end + 1 == c:
#             print(cnt + 1)
#         elif start + 1 == r and end == c:
#             print(cnt + 2)
#         else:
#             print(cnt + 3)
#         sys.exit()
#
# divncon(0, 0, N * 2)

# 반복으로도 풀 수 있다.
N, r, c = map(int, input().split())
cnt = 0

while N > 1:
    size = (2 ** N) // 2
    if r < size and c < size: # 2사분면
        pass
    elif r < size and c >= size: # 1사분면
        cnt += size ** 2
        c -= size
    elif r >= size and c < size: # 3사분면
        cnt += size ** 2 * 2
        r -= size
    elif r >= size and c >= size: # 4사분면
        cnt += size ** 2 * 3
        r -= size
        c -= size
    N -= 1

if r == 0 and c == 0:
    print(cnt)
if r == 0 and c == 1:
    print(cnt + 1)
if r == 1 and c == 0:
    print(cnt + 2)
if r == 1 and c == 1:
    print(cnt + 3)