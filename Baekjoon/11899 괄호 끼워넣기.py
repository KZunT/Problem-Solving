word = input().rstrip()
cnt = len(word)

while True:
    word = word.replace("()", "")
    cnt -= 1

    if cnt == 0:
        print(len(word))
        break
