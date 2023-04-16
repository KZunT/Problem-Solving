from itertools import permutations

N = int(input())
K = int(input())

cards = [input() for _ in range(N)]

result = set()

for num in permutations(cards, K):
    result.add(''.join(num))

print(len(result))
