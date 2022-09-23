def solution(participant, completion):
    # 시간초과 방지를 위해 sort 해야함
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant) - 1]

# collections 사용한 풀이 추가

# import collections
#
# 
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]