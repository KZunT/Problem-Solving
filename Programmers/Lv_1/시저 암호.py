def solution(s, n):
    answer = ''

    # 65 ~ 90 = A ~ Z  , 97 ~ 122 = a ~ z
    ch = 0

    for i in s:

        if ord(i) == 32:
            answer = answer + " "
            continue

        if 64 < ord(i) < 91:
            ch = ord(i) + n
            if ch > 90:
                ch = ch - 26
            answer = answer + chr(ch)

        if 96 < ord(i) < 123:
            ch = ord(i) + n
            if ch > 122:
                ch = ch - 26
            answer = answer + chr(ch)

    return answer