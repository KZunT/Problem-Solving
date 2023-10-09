import sys

input = sys.stdin.readline

N, M = map(int, input().split())

cards = list(map(int, input().split()))

for _ in range(M):
    cards.sort()
    cards[0] = cards[1] = cards[0] + cards[1]

print(sum(cards))
