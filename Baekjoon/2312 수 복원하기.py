T = int(input())

for _ in range(T):
    N = int(input())
    prime = {}

    for i in range(2, N + 1):
        while True:
            if N % i == 0:
                N = N // i
                if i in prime:
                    prime[i] += 1
                else:
                    prime[i] = 1
            else:
                break

    for key, value in prime.items():
        print(key, value)
