# from collections import Counter

# # def solution(orders, course):
# #     answer = []

# #     print(sorted(orders,key=len))

# #     for i ,first in enumerate(orders):
# #         for j, sec in enumerate(orders):
# #             if i != j:
# #                 menu = "".join(sorted(list(set(first) & set(sec))))
# #                 if len(menu) in course:
# #                     answer.append(menu)

# #     print(Counter(answer))

# #     return sorted(answer)

# def solution(orders, course):
#     answer = []

#     orders.sort(key=len)

#     for i in range(len(orders)-1):
#         for j in range(i+1,len(orders)):
#             menu = "".join(sorted(list(set(orders[i]) & set(orders[j]))))
#             if menu not in answer and len(menu) in course:
#                 answer.append(menu) # 메뉴 후보군 추가

#     res = []

#     for menu in answer:
#         for order in orders:
#             if all(m in order for m in menu):   # 메뉴 빈도수 파악
#                 res.append(menu)

#     maxi = dict()
#     res = Counter(res)

#     print(res)
#     for c in course:
#         for name, num in res.items():
#             if len(name) == c:
#                 if c not in maxi:
#                     maxi[c] = num

#                 if maxi[c] < num:
#                     maxi[c] = num

#     result = []

#     for name,num in res.items():
#         if num == maxi[len(name)]:
#             result.append(name)

#     return sorted(result)

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_candidates = Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)