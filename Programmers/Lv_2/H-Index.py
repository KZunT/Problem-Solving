def solution(citations):
    answer = 0

    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] < i + 1:  # n번 인덱스가 n번 인용이 되었는지 확인
            return i

    return len(citations)  # 반례, 모든 citations의 값이 list의 길이와 같으면 위의 for문에서 답이 나오지 않음.