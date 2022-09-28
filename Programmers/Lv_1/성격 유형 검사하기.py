def solution(survey, choices):
    answer = ''
    score = [3, 2, 1, 0, 1, 2, 3]
    cha_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for sur, choice in zip(survey, choices):
        if choice < 4:
            cha_dict[sur[0]] += score[choice - 1]
        if choice > 4:
            cha_dict[sur[1]] += score[choice - 1]
        if choice == 4:
            pass

    if cha_dict['R'] >= cha_dict['T']:
        answer += 'R'
    else:
        answer += 'T'

    if cha_dict['C'] >= cha_dict['F']:
        answer += 'C'
    else:
        answer += 'F'

    if cha_dict['J'] >= cha_dict['M']:
        answer += 'J'
    else:
        answer += 'M'

    if cha_dict['A'] >= cha_dict['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer