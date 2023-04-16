import math

T = int(input())

for _ in range(T):
    numbers = list(map(int, input().split()))
    gcd_sum = 0
    for i in range(1, len(numbers)):
        for j in range(i + 1, len(numbers)):
            gcd_sum += math.gcd(numbers[i], numbers[j])

    print(gcd_sum)
