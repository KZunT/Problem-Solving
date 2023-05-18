N = int(input())
start, end = 1, 1
cnt = 0
answer = 1

while end != N:

    if answer < N:
        end += 1
        answer += end

    elif answer > N:
        answer -= start
        start += 1

    else:
        cnt += 1
        end += 1
        answer += end

print(cnt + 1)
