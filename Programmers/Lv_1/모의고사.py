def solution(answers):
    answer = []
    result = [0, 0, 0]
    f_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    s_list = [2, 1, 2, 3, 2, 4, 2, 5]
    t_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        f_list.append(f_list[i])
        s_list.append(s_list[i])
        t_list.append(t_list[i])

        if answers[i] == f_list[i]:
            result[0] = result[0] + 1
        if answers[i] == s_list[i]:
            result[1] = result[1] + 1
        if answers[i] == t_list[i]:
            result[2] = result[2] + 1

    for i, v in enumerate(result):
        if v == max(result):
            answer.append(i + 1)

    return answer

# 간결화 가능