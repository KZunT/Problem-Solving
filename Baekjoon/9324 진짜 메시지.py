for _ in range(int(input())):
    word = input()
    msg = [0 for _ in range(26)]
    answer = 'OK'
    check = False

    for i in range(len(word)):
        if check:
            check = False
            continue

        msg[ord(word[i]) - 65] += 1

        if msg[ord(word[i]) - 65] == 3:
            if i == len(word) - 1 or word[i] != word[i + 1]:
                answer = 'FAKE'
                break

            check = True
            msg[ord(word[i]) - 65] = 0

    print(answer)
