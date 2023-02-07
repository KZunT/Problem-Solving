import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pokemon = dict()

for i in range(1,N+1):
    name = input().rstrip()

    pokemon[name] = i
    pokemon[i] = name

for _ in range(M):
    order = input().rstrip()

    if order.isdigit():
        print(pokemon[int(order)])
    else:
        print(pokemon[order])