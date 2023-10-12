N = int(input())
stack = []
cnt = 1

stand = list(map(int, input().split()))

while stand:
    if cnt == stand[0]:
        cnt += 1
        stand.pop(0)
    else:
        stack.append(stand.pop(0))

    while stack:
        if stack[-1] == cnt:
            stack.pop()
            cnt += 1
        else:
            break

print('Nice' if not stack else 'Sad')

