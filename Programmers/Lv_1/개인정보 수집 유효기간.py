def solution(today, terms, privacies):
    answer = []

    term_dict = {}

    for term in terms:
        name, month = term.split()
        term_dict[name] = month

    for i, privacy in enumerate(privacies):
        date, term_name = privacy.split()

        year, month, day = date.split('.')

        new_month = int(month) + int(term_dict[term_name])

        if new_month > 12:
            new_year = int(year) + new_month // 12
            new_month = new_month % 12
        else:
            new_year = year

        if new_month == 0:
            new_year = new_year - 1
            new_month = 12

        new_day = day

        cur_year, cur_month, cur_day = today.split('.')

        if int(cur_year) > int(new_year):
            answer.append(i + 1)
        elif int(cur_year) == int(new_year) and int(cur_month) > int(new_month):
            answer.append(i + 1)
        elif int(cur_year) == int(new_year) and int(cur_month) == int(new_month) and int(cur_day) >= int(new_day):
            answer.append(i + 1)

    return answer
