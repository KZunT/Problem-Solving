T = int(input())

for _ in range(T):
    plain_text = []
    N = int(input())
    p_key_1 = list(input().split())
    p_key_2 = list(input().split())
    cryptogram = list(input().split())

    word = {}

    for idx in p_key_2:
        word[p_key_1.index(idx)] = cryptogram.pop(0)

    print(" ".join(dict(sorted(word.items())).values()))
