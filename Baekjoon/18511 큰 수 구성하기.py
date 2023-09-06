from itertools import product

N, K = map(int, input().split())
length = len(str(N))
numbers = list(input().split())

while True:
    num_list = list(product(numbers, repeat=length))
    result = []

    for num in num_list:
        if int("".join(num)) <= N:
            result.append(int("".join(num)))

    if len(result) >= 1:
        print(max(result))
        break

    else:
        length -= 1
