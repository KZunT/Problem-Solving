T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    X = int(''.join(list(input().split())))
    Y = int(''.join(list(input().split())))
    data = list(map(int, input().split()))
    data += data[:M]
    answer = 0

    for i in range(N):
        check = int(''.join(map(str, data[i:i + M])))
        if X <= check <= Y:
            answer += 1

    print(answer)
