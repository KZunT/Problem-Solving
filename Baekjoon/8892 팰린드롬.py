T = int(input())


def palindrome():
    N = int(input())
    words = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i != j:
                new_word = words[i] + words[j]
                if new_word == new_word[::-1]:
                    return new_word

    return 0


for _ in range(T):
    answer = palindrome()
    print(0) if answer == 0 else print(answer)
