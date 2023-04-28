import sys
input = sys.stdin.readline
stack = list(input().rstrip())
result = []

N = int(input())

for _ in range(N):
    command = input().rstrip()

    if command[0] == 'P':
        stack.append(command[2])

    elif command[0] == 'L' and stack != []:
        result.append(stack.pop())

    elif command[0] == 'D' and result != []:
        stack.append(result.pop())

    elif command[0] == 'B' and stack != []:
        stack.pop()

print(''.join(stack + list(reversed(result))))