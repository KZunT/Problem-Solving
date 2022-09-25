def solution(numbers, hand):
    answer = ''
    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']] # 키패드 생성
    current_left = '*'
    current_right = '#'

    for num in numbers:

        for idx, row in enumerate(pad):
            if num in row:
                num_coord = idx, row.index(num)
            if current_right in row:
                r_coord = idx, row.index(current_right)
            if current_left in row:
                l_coord = idx, row.index(current_left)
        # 번호간 거리 계산 하여 우선순위 설정
        r_d = abs(num_coord[0] - r_coord[0]) + abs(num_coord[1] - r_coord[1])
        l_d = abs(num_coord[0] - l_coord[0]) + abs(num_coord[1] - l_coord[1])
        # 우선순위대로 입력
        if num in [1, 4, 7]:
            answer = answer + "L"
            current_left = num
        elif num in [3, 6, 9]:
            answer = answer + "R"
            current_right = num
        else:
            if r_d == l_d:
                if hand == "left":
                    answer = answer + "L"
                    current_left = num
                else:
                    answer = answer + "R"
                    current_right = num

            else:
                if r_d > l_d:
                    answer = answer + "L"
                    current_left = num
                else:
                    answer = answer + "R"
                    current_right = num

    return answer