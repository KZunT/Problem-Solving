import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
food = []

for _ in range(N):
    food.append(list(map(int, input().split())))

recipe = []

for i in range(1, N + 1):
    recipe.append(combinations(food, i))

answer = 1E+6

for line in recipe:
    for each in line:
        sour = 1
        bitter = 0
        for e in each:
            sour *= e[0]
            bitter += e[1]

        answer = min(answer, abs(sour - bitter))

print(answer)
