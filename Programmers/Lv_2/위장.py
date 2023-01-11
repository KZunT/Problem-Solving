def solution(clothes):
    answer = 1

    c_dict = dict()

    for cloth in clothes:
        if cloth[1] in c_dict:
            c_dict[cloth[1]] += 1
        else:
            c_dict[cloth[1]] = 2  # 옷이 주어졌을경우, 입는 경우 or 안입는 경우가 있기 때문에 2부터 시작

    for c, num in c_dict.items():
        answer *= num

    return answer - 1  # 모든 옷을 안입는 경우를 제거