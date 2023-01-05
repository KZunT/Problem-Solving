def solution(s):
    lis = []
    for v in s:
        if v == '(':
            lis.append(v)
        if v == ')':
            try:
                lis.pop()
            except:
                return False
    return len(lis) == 0
