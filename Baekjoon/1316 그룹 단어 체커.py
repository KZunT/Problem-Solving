n = int(input())

cnt = n

for i in range(n):
    word = input()

    for w in range(len(word)-1):

        if word[w] == word[w + 1]: # 다음 나올 알파벳이 현재 알파벳과 같다면 패스
            pass
        elif word[w] in word[w+1:]: # 다음 알파벳이 현재와 같지 않고, 다음 알파벳 이후에 현재 알파벳이 나오면 중복이므로 그룹 단어가 아님
            cnt -= 1
            break

print(cnt)
