N = int(input())

prime_list = []

num = 1

while True:
    if num > 120:
        break

    for i in range(2, num + 1):
        if num % i == 0:
            if num == i:
                prime_list.append(i)
            break
    num += 1

idx = 0

while True:
    if N < (prime_list[idx] * prime_list[idx + 1]):
        break
    idx += 1

print(prime_list[idx] * prime_list[idx + 1])
