from itertools import permutations


def isprime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(n ** (0.5)) + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    answer = []

    for i in range(1, len(numbers) + 1):
        per = list(permutations(numbers, i))

        for p in per:
            num = int(''.join(p))
            if num not in answer:
                if isprime(num):
                    answer.append(num)

    return len(answer)
