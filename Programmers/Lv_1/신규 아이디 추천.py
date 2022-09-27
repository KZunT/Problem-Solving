def solution(new_id):
    answer = ''

    new_id = new_id.lower()

    for w in new_id:
        if w.isalpha() or w.isdigit() or w in ['-', '_', '.']:
            answer = answer + w

    while (True):
        temp = answer
        answer = answer.replace('..', '.')

        if temp == answer:
            break

    answer = answer.strip('.')

    if answer == '':
        answer = "a"

    if len(answer) > 15:
        answer = answer[:15]

    answer = answer.strip('.')

    if len(answer) < 3:
        while (True):
            answer = answer + answer[-1]
            if len(answer) == 3:
                break

    return answer


# 정규 표현식 사용한 코드

# import re
#
# def solution(new_id):

#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])

#     return st