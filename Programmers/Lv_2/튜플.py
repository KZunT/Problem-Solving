def solution(s):
    answer = []

    setlist = s[2:-2].split('},{')
    setlist.sort(key=len)

    for i in range(len(setlist)):
        num = set(setlist[i].split(',')) - set(answer)
        answer.append(list(num)[0])

    return list(map(int, answer))