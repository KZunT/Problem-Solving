# from collections import deque
#
# N = int(input())
#
# q = deque()
#
# for i in range(1, N + 1):
#     q.append(i)
#
# while True:
#     if len(q) == 1:
#         break
#
#     q.popleft()
#
#     if len(q) == 1:
#         break
#
#     q.append(q.popleft())
#
# print(q[0])


#시간이 빠른 코드 추가 (규칙을 이용)

n = int(input())
num = 2
while True:
    if n == 1 or n == 2:
        print(n)
        break
    num *= 2
    if num >= n:
        print((n - (num // 2)) * 2)
        break