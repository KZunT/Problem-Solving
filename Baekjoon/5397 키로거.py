N = int(input())

for _ in range(N):
    left = []
    right = []
    command = input()

    for c in command:
        if c == '<':
            if left:
                right.append(left.pop())
        elif c == '>':
            if right:
                left.append(right.pop())
        elif c == '-':
            if left:
                left.pop()
        else:
            left.append(c)

    left.extend(reversed(right))

    print(''.join(left))
