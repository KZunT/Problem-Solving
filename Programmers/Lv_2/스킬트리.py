def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        skt = list(skill)
        for t in tree:
            if t in skt and t == skt[0]:
                skt.pop(0)
            if t in skt and t != skt[0]:
                break
        else:
            answer += 1
    return answer