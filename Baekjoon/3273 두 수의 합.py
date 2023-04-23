N = int(input())
sequence = list(map(int, input().split()))
X = int(input())

sequence.sort()

answer = 0
start = 0
end = N - 1

while start < end:
    sum_pair = sequence[start] + sequence[end]

    if sum_pair == X:
        answer += 1
        start += 1

    elif sum_pair > X:
        end -= 1

    else:
        start += 1

print(answer)
