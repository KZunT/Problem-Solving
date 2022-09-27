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