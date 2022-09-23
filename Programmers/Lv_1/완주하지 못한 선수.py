def solution(participant, completion):
    # 시간초과 방지를 위해 sort 해야함
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant) - 1]
