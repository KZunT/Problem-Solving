from itertools import permutations

N = int(input())

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(data, 3))

for _ in range(N):
    qus, s, b = map(int, input().split())
    qus = list(str(qus))
    remove = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= remove
        for j in range(3):
            if num[i][j] == qus[j]:
                strike += 1
            elif qus[j] in num[i]:
                ball += 1

        if (strike != s) or (ball != b):
            num.remove(num[i])
            remove += 1

print(len(num))