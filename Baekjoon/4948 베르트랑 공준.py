# pypy3 일 경우만 시간초과가 뜨지 않는다..

def brt(n):
    cnt = (2 * n) - (n + 1)
    for i in range(n + 1, 2 * n):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:  # 소수가 아닌 경우
                cnt -= 1
                break
    return cnt


while True:
    num = int(input())
    if num == 0:
        break
    elif num == 1:
        print(1)
    else:
        print(brt(num))

# 시간초과 해결 코드.. 어째서?
# def getPrimaryNum_Eratos(N):
#     nums = [True] * (N)
#     for i in range(2, int(N ** 0.5) + 1):
#         if nums[i] == True:
#             for j in range(i + i, N, i):
#                 nums[j] = False
#
#     return [i for i in range(2, N) if nums[i] == True]
#
#
# while True:
#     N = int(input())
#
#     if N == 0:
#         break
#
#     prime_list = getPrimaryNum_Eratos(2 * N + 1)
#     answer_list = [num for num in prime_list if num > N]
#
#     print(len(answer_list))
