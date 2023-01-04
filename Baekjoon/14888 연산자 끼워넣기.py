# # 시간초과로 pypy3에서만 맞음
#
# from itertools import permutations
#
# def cal(a, b, o):
#     if o == 0:
#         return a + b
#     if o == 1:
#         return a - b
#     if o == 2:
#         return a * b
#     if o == 3:
#         if a < 0:
#             a = a * -1
#             return a // b * -1
#         return a // b
#
#
# N = int(input())
# A = list(map(int, input().split()))
# op = list(map(int, input().split()))
#
# op_list = []
# result_list = []
#
# for i in range(len(op)):
#     op_list.extend([i] * op[i])
#
# for o in permutations(op_list):
#     a = A[0]
#     for i in range(len(A) - 1):
#         result = cal(a, A[i + 1], o[i])
#         a = result
#     result_list.append(result)
#
# print(max(result_list))
# print(min(result_list))

# dfs 이용 코드

n = int(input())
number = list(map(int, input().split()))
op = list(map(int, input().split()))
minR = int(1e9)
maxR = -int(1e9)

answer = number[0]

def dfs(idx):
    global answer
    global minR, maxR

    if idx == n:
        if answer > maxR:
            maxR = answer
        if answer < minR:
            minR = answer
        return

    for i in range(4):
        tmp = answer
        if op[i] > 0:
            if i == 0:
                answer += number[idx]
            elif i == 1:
                answer -= number[idx]
            elif i == 2:
                answer *= number[idx]
            else:
                if answer >= 0:
                    answer //= number[idx]
                else:
                    answer = (-answer // number[idx]) * -1

            op[i] -= 1
            dfs(idx+1)
            answer = tmp
            op[i] += 1


dfs(1)
print(maxR)
print(minR)