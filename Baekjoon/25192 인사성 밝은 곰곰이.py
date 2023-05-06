N = int(input())

talk = {}

cnt = 0

for _ in range(N):
    message = input()

    if message == "ENTER":
        for key, value in talk.items():
            if value == 1:
                cnt += 1
        talk = {}
    else:
        if message not in talk:
            talk[message] = 1

for key, value in talk.items():
    if value == 1:
        cnt += 1

print(cnt)

# 왜 틀렸을까..?

# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# s = set()
# cnt = 0
# first = input()  # 첫 ENTER 입력받기
#
# for _ in range(N - 1):
#     message = input()
#     if message == 'ENTER':
#         cnt += len(s)
#         s.clear()
#
#     else:
#         s.add(message)
#
# cnt += len(s)
#
# print(cnt)