def solution(N, stages):

    fail = {}
    for num in range(1, N + 1):
        non_clear = 0
        clear = 0

        for stage in stages:
            if stage >= num:
                clear += 1
            if stage == num:
                non_clear += 1

        if clear == 0:
            fail[num] = 0
        else:
            fail[num] = non_clear / clear

    fail = sorted(fail.items(), key=lambda x: x[1], reverse=True)
    answer = list(dict(fail).keys())

    return answer