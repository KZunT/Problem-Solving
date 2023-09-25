fibo = [0, 1]
for i in range(2, 50):
    fibo.append(fibo[i - 2] + fibo[i - 1])

T = int(input())

for _ in range(T):
    N = int(input())

    numbers = []

    while N > 0:
        for k in range(50):
            if (fibo[k] <= N):
                temp = fibo[k]

        N = N - temp
        numbers.append(temp)
        numbers.sort()

    for number in numbers:
        print(number, end=' ')
