def solution(s):
    answer = 1
    word = s[0]

    x_cnt = 0
    nx_cnt = 0

    for i in range(len(s) - 1):
        if s[i] == word:
            x_cnt += 1
        else:
            nx_cnt += 1

        if x_cnt == nx_cnt:
            answer += 1
            word = s[i + 1]
            x_cnt = 0
            nx_cnt = 0

    return answer

# def solution(s):
#     answer = 0

#     x=0
#     nx=0

#     for i in s:
#         if x==nx:
#             answer+=1
#             word=i

#         if word==i:
#             x+=1
#         else:
#             nx+=1

#     return answer
