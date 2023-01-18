# from collections import Counter

# def solution(str1, str2):
#     answer = 0
#     str1 = str1.upper()
#     str2 = str2.upper()

#     st1_list = []
#     st2_list = []

#     for i in range(len(str1)-1):
#         if str1[i:i+2].isalpha():
#             st1_list.append(str1[i:i+2])

#     for i in range(len(str2)-1):
#         if str2[i:i+2].isalpha():
#             st2_list.append(str2[i:i+2])

#     if st1_list == [] and st2_list == []:
#         return 65536

#     inter = 0
#     union = 0

#     cst1 = Counter(st1_list)
#     cst2 = Counter(st2_list)

#     for cs , num in cst1.items():
#         if cs in cst2:
#             inter += min(cst1[cs] , cst2[cs])
#             union += max(cst1[cs] , cst2[cs])
#             cst1[cs] = cst2[cs] = 0

#     for cs , num in cst1.items():
#             union += num
#     for cs , num in cst2.items():
#             union += num
#     print(inter, union)
#     return int(inter/union * 65536)


import re
import math


def solution(str1, str2):
    str1 = [str1[i:i + 2].lower() for i in range(0, len(str1) - 1) if not re.findall('[^a-zA-Z]+', str1[i:i + 2])]
    str2 = [str2[i:i + 2].lower() for i in range(0, len(str2) - 1) if not re.findall('[^a-zA-Z]+', str2[i:i + 2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0:
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum / hap_sum) * 65536)