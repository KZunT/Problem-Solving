# N = int(input())
#
# for _ in range(N):
#
#     n = input()
#     card_list = list(map(str,input().split()))
#
#     s = ''
#
#     first_card = card_list.pop(0)
#
#     s += first_card
#
#     for card in card_list:
#
#         if first_card <= card:
#             s += card
#         else:
#             s = card + s
#     print(s)
#
# 위의 코드 왜 안되는지..

testcase = int(input())

for _ in range(testcase):
    N = int(input())
    card_list = list(input().split())

    ans_lst = [card_list.pop(0)]
    for i in card_list:
        if ans_lst[0] >= i:
            ans_lst.insert(0, i)
        else:
            ans_lst.append(i)

    for i in ans_lst:
        print(i, end='')
    print()
