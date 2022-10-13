document = input()
word = input()

cnt = 0

while True:
    index = document.find(word)

    if index == -1: # 문서 내에 단어가 없을경우 종료
        break

    document = document[index + len(word):]  # 찾았으면 찾은단어를 제외하고, 문서 업데이트

    cnt += 1

print(cnt)