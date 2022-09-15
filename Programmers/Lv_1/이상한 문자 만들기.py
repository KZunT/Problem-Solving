def solution(s):
    answer = ''

    list = s.split(" ")

    for i in list:

        for j in range(len(i)):

            if j % 2 == 0:
                answer = answer + i[j].upper()
            else:
                answer = answer + i[j].lower()

        answer = answer + " "

    idx = len(answer) - 1

    return answer[:idx]