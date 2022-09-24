from typing import List


def solution(queries: List[List[int]]) -> int:
    answer = 0
    arr_dict = {}
    len_dict = {}

    for query in queries:
        arr_num = query[0]
        arr_dict[arr_num] = 0
        len_dict[arr_num] = 0

    # print(arr_dict)

    for query in queries:
        arr_num = query[0]
        add_ele = query[1]

        # print(arr_num,"추가")

        if arr_dict[arr_num] + add_ele > len_dict[arr_num]:
            answer = answer + arr_dict[arr_num]
            # print(arr_num,"복사",arr_dict[arr_num])

            i = 0
            while (True):
                if 2 ** i >= arr_dict[arr_num] + add_ele:
                    len_dict[arr_num] = 2 ** i
                    break
                i = i + 1

        arr_dict[arr_num] = arr_dict[arr_num] + add_ele

    # print(len_dict)

    return answer