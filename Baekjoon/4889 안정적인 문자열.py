answer = []

while True:
    stack = []
    cnt = 0
    N = input()
    if '-' in N:
        break
    for i in range(len(N)):
        if not stack and N[i] == '}':
            cnt += 1
            stack.append('{')
        elif stack and N[i] == '}':
            stack.pop()
        else:
            stack.append(N[i])
    cnt += len(stack) // 2
    answer.append(cnt)

for i in range(len(answer)):
    print(i + 1, '. ', answer[i], sep='')
