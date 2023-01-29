stick = input()

stick = stick.replace('()','l')

result = 0
stack = []


for i in stick:
    if i == 'l':
        result += len(stack)
    if i == '(':
        stack.append(i)
    if i == ')':
        result += 1
        stack.pop()

print(result)