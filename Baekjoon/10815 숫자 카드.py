M = int(input())
num_list = list(map(int,input().split()))
N = int(input())
card_list = list(map(int,input().split()))

num_list.sort()

answer = [0] * N

for i, card in enumerate(card_list):
    start ,end = 0, M-1

    while start <= end:
        mid = (start + end) // 2

        if num_list[mid] > card:
            end = mid - 1
        elif num_list[mid] < card:
            start = mid + 1
        else:
            answer[i] = 1
            break

print(' '.join(map(str,answer)))


## 딕셔너리 사용도 가능..
# import sys
#
# N = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# checks = list(map(int, sys.stdin.readline().split()))
#
# _dict = {}  # 속도는 dictionary!
# for i in range(len(cards)):
#     _dict[cards[i]] = 0  # 아무 숫자로 mapping
#
# for j in range(M):
#     if checks[j] not in _dict:
#         print(0, end=' ')
#     else:
#         print(1, end=' ')