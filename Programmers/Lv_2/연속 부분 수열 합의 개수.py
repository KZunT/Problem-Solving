def solution(elements):
    answer = []
    elist = elements * 2

    for i in range(1, len(elements) + 1):  # 원소개수
        for j in range(len(elements)):  # 원소 인덱스
            answer.append(sum(elist[j:j + i]))

    return len(list(set(answer)))