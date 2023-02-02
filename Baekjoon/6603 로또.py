def make_lotto(start):

    if len(lotto) == 6:
        print(" ".join(map(str,lotto)))

    for i in range(start,K):
        lotto.append(S[i])
        make_lotto(i+1)
        lotto.pop()


while True:
    num = list(map(int, input().split()))

    K = num[0]

    if K == 0:
        break

    S = num[1:]

    lotto = []

    make_lotto(0)
    print()