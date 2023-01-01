from collections import deque
import sys

deck = deque()

N = int(input())

for _ in range(N):
    command = sys.stdin.readline().split() # input() 으로하면 시간초과..
    order = command[0]

    if order == 'push_front':
        deck.appendleft(int(command[1]))
    if order == 'push_back':
        deck.append(int(command[1]))
    if order == 'pop_front':
        if deck:
            print(deck.popleft())
        else:
            print(-1)
    if order == 'pop_back':
        if deck:
            print(deck.pop())
        else:
            print(-1)
    if order == 'size':
        print(len(deck))
    if order == 'empty':
        if deck:
            print(0)
        else:
            print(1)
    if order == 'front':
        if deck:
            print(deck[0])
        else:
            print(-1)
    if order == 'back':
        if deck:
            print(deck[-1])
        else:
            print(-1)