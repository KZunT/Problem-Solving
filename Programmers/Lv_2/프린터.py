from collections import deque


def solution(priorities, location):
    cnt = 1
    index = deque(list(range(len(priorities))))
    priorities = deque(priorities)

    while True:
        if priorities == []:
            break

        if priorities[0] == max(priorities):
            if index[0] == location:
                return cnt
            priorities.popleft()
            index.popleft()

            cnt += 1

        else:
            priorities.append(priorities.popleft())
            index.append(index.popleft())

    return cnt