S = input()

word_list = []

for i in range(0, len(S)):
    word_list.append(S[i:])

word_list.sort()

for w in word_list:
    print(w)