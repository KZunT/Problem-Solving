def solution(s):
    answer = []
    word = dict()

    for i in range(len(s)):
        if s[i] in word:
            answer.append(i - word[s[i]])
            word[s[i]] = i
        else:
            answer.append(-1)
            word[s[i]] = i

    return answer
