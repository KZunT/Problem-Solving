# def solution(numbers, target):
#     answer = 0
#     node = [0]

#     for num in numbers:
#         tmp = []
#         for n in node:
#             tmp.append(n + num)
#             tmp.append(n - num)
#         node = tmp

#     return node.count(target)


# #DFS 풀이
# def solution(numbers, target):
#     answer = DFS(numbers, target, 0)
#     return answer

# def DFS(numbers, target, depth):
#     answer = 0
#     if depth == len(numbers):
#         #print(numbers)
#         if sum(numbers) == target:
#             return 1
#         else: return 0
#     else:
#         answer += DFS(numbers, target, depth+1)
#         numbers[depth] *= -1
#         answer += DFS(numbers, target, depth+1)
#         return answer

from itertools import product


def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
