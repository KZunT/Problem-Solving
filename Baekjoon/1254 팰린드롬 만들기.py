S = input()

for i in range(len(S)):  # i = 기준점
    if S[i:] == S[i:][::-1]:
        print(len(S) + i)
        break
