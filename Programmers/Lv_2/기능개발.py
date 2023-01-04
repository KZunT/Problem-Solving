def solution(progresses, speeds):
    answer = []

    while (True):

        if progresses == []:
            break

        cnt = 0

        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

        if progresses[0] >= 100:

            while (True):
                cnt = cnt + 1
                progresses.pop()
                speeds.pop()

                if progresses == []:
                    answer.append(cnt)
                    break

                if progresses[0] < 100:
                    answer.append(cnt)
                    break

    return answer
