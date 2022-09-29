def solution(id_list, report, k):

    answer = [0 for i in range(len(id_list))]
    report_dict = {id: [] for id in id_list}

    report = list(set(report))

    for rep in report:
        report_dict[rep.split(' ')[1]].append(rep.split(' ')[0])

    for key, value in report_dict.items():
        if len(value) >= k:
            for v in value:
                answer[id_list.index(v)] = answer[id_list.index(v)] + 1

    return answer