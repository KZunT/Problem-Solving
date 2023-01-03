def solution(food):
    answer = '0'
    for i in reversed(range(len(food))):
        cnt = food[i] // 2
        answer = str(i) * cnt + answer + str(i) * cnt
    return answer
