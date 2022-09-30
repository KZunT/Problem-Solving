N = input()

origin = N

cnt = 0

while (True):

    if int(N) < 10:
        N = '0' + N

    N = str(int(str(int(N) % 10) + str((int(N) // 10 + int(N) % 10) % 10)))

    cnt += 1

    if N == origin:
        break

print(cnt)

# 입력의 자료형을 잘 생각하자

# n = int(input())
# m = n
# i = 0
# while True:
#     m = m % 10 * 10 + (m % 10 + m // 10) % 10
#     i += 1
#     if m == n:
#         break
# print(i)