N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

num = 1

stack = []
order = []

while True:
    if stack == []:
        stack.append(num)
        num += 1
        order.append('+')
    else:
        if stack[-1] != arr[0]:
            stack.append(num)
            num += 1
            order.append('+')

        if stack[-1] == arr[0]:
            arr.pop(0)
            stack.pop(-1)
            order.append('-')

    if num > N:
        break

for _ in range(len(stack)):
    if stack[-1] == arr[0]:
        arr.pop(0)
        stack.pop(-1)
        order.append('-')
    else:
        order = 'NO'
        break

if order == 'NO':
    print(order)
else:
    for o in order:
        print(o)
