def solution(s):
    s = s.title()
    s = list(s)

    for i in range(len(s) - 1):
        if s[i].isdigit():
            s[i + 1] = s[i + 1].lower()

    return ''.join(s)
