def solution(people, limit):
    answer = 0

    people.sort()

    start = 0
    end = len(people) - 1

    while start <= end: # 가장 몸무게가 적은사람과 많이나가는 사람으로 섞어서 태우기

        if people[start] + people[end] <= limit: # 구명보트에 최대 2명까지밖에 못탐
            start += 1
            end -= 1
        else:
            end -= 1

        answer += 1

    return answer