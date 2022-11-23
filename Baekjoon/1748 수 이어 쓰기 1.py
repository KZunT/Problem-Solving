# N = int(input())
#
# s = ''
#
# for i in range(1, N + 1):
#     s += str(i)
#
# print(len(s))
#
# 위의 코드는 시간초과

N = input()

comp = len(N) - 1

answer = 0

for i in range(comp):
    answer += 9 * (10 ** i) * (i + 1)
    i += 1
answer += ((int(N) - (10 ** comp)) + 1) * (comp + 1)

print(answer)