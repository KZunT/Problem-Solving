# def solution(prices):
#     answer = []

#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[i] > prices[j]:
#                 answer.append(j-i)
#                 break
#         else:
#             answer.append(j-i)

#     return answer


def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
