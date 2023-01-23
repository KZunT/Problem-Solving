# def solution(n):
#     num = ['1','2','4']
#     answer = ""

#     while n > 0:
#         n -= 1
#         answer = num[n % 3] + answer
#         n //= 3

#     return answer


def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]