import sys

input = sys.stdin.readline

while True:
    test = input().rstrip()

    if not test:
        break

    S, T = test.split()

    cnt = 0

    for i in range(len(T)):
        if T[i] == S[cnt]:
            cnt += 1
            if cnt == len(S):
                print('Yes')
                break
    else:
        print('No')
