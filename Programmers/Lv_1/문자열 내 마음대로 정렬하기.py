def solution(strings, n):
    strings.sort()

    le = len(strings)

    for i in range(le - 1):
        for j in range(le - i - 1):
            if strings[j][n] > strings[j + 1][n]:
                strings[j], strings[j + 1] = strings[j + 1], strings[j]

    return strings