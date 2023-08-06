from collections import deque


def solution(queue1, queue2):
    answer = 0

    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    while True:
        if sum1 == sum2:
            return answer

        if answer == 4 * len(q1):  # 모든 탐색을 끝내고 제자리로 돌아오는 경우
            return -1

        if sum1 > sum2:
            value = q1.popleft()
            q2.append(value)
            sum1 -= value
            sum2 += value
        else:
            value = q2.popleft()
            q1.append(value)
            sum1 += value
            sum2 -= value

        answer += 1
