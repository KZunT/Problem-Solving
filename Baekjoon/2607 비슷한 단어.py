N = int(input())
target_word = list(input())
answer = 0

for _ in range(N - 1):
    compare_word = target_word[:]
    new_word = input()
    cnt = 0

    for w in new_word:
        if w in compare_word:
            compare_word.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare_word) < 2:
        answer += 1

print(answer)
