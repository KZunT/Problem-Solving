word = input()
target = 'UCPC'
idx = 0

for w in word:
    if w == target[idx]:
        idx += 1
    if idx == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')
