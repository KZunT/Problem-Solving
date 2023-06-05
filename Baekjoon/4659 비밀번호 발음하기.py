vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    pw = input()
    if pw == 'end':
        break

    vowel_check = False
    vowel_cnt = 0
    consonant_cnt = 0
    string_check = True

    for i in range(len(pw)):
        if pw[i] in vowels:
            vowel_check = True
            vowel_cnt += 1
            consonant_cnt = 0
        else:
            consonant_cnt += 1
            vowel_cnt = 0
        if consonant_cnt == 3 or vowel_cnt == 3:
            string_check = False
            break
        if i != 0:
            if pw[i] == pw[i - 1] and pw[i] not in ['e', 'o']:
                vowel_check = False
                break

    if string_check and vowel_check:
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")
