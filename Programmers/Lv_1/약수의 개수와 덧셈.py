def solution(left, right):
    answer = 0

    for num in range(left, right + 1):

        divide_list = []

        for i in range(1, num + 1):
            if num % i == 0:
                divide_list.append(i)

        if len(divide_list) % 2 == 0:
            answer = answer + num
        else:
            answer = answer - num

    return answer