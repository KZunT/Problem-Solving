N = int(input())
exps = list(input())
numbers = [int(input()) for _ in range(N)]
stack = []

for exp in exps:
    if 'A' <= exp <= 'Z':
        number = ord(exp) - ord('A')
        stack.append(numbers[number])
    else:
        B = stack.pop()
        A = stack.pop()

        if exp == '+':
            stack.append(A + B)
        elif exp == '-':
            stack.append(A - B)
        elif exp == '*':
            stack.append(A * B)
        elif exp == '/':
            stack.append(A / B)

print("%.2f" % stack[0])
