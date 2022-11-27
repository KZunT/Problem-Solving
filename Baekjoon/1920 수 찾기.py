N = int(input())
b_list = list(map(int, (input().split())))
M = int(input())
Target_list = list(map(int, (input().split())))

b_list.sort()


def binary(Target, b_list, start, end):
    if start > end:  # 못 찾은경우
        return 0
    mid = (start + end) // 2  # 중간점 지정
    if Target == b_list[mid]:
        return 1  # 찾은 경우
    elif Target < b_list[mid]:
        return binary(Target, b_list, start, mid - 1)
    else:
        return binary(Target, b_list, mid + 1, end)


for T in Target_list:
    start = 0
    end = len(b_list) - 1
    print(binary(T, b_list, start, end))
