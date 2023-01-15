def solution(s):
    answer = 0

    braket = {')': '(', '}': '{', ']': '['}

    for i in range(len(s)):
        string = s[i:] + s[:i]
        stack = []

        for i in string:
            if stack == []:
                stack.append(i)
            elif i in [')', ']', '}']:
                if braket[i] in stack:
                    # stack.remove(braket[i])
                    stack.pop()
                else:
                    break
            else:
                stack.append(i)

        if stack == []:
            answer += 1

    return answer