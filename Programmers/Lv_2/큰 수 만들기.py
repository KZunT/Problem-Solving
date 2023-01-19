# def solution(number, k):
#     answer = ''
#     num_list = list(map(int,number))
#     stack = []
#     remove = 0
#     i = 0
#     while True:
#         if remove == k:
#             stack.extend(num_list[i:])
#             break

#         if i == len(num_list):
#             break

#         if stack == []:
#             stack.append(num_list[i])
#             i +=1
#         else:
#             if stack[-1] < num_list[i]:
#                 stack.pop()
#                 remove +=1
#             else:
#                 stack.append(num_list[i])
#                 i += 1

#     return ''.join(list(map(str,stack)))[:len(number)-k]

def solution(number, k):
    answer = []  # Stack

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(answer) - k])