def solution(ingredient):
    hamberger = []
    answer = 0
    for i in ingredient:
        hamberger.append(i)
        if hamberger[-4:] == [1, 2, 3, 1]:
            answer += 1
            del hamberger[-4:]
    return answer
