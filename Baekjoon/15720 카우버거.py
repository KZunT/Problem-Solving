B, C, D = map(int, input().split())

burgers = sorted(list(map(int, input().split())), reverse=True)
sides = sorted(list(map(int, input().split())), reverse=True)
drinks = sorted(list(map(int, input().split())), reverse=True)

total = 0
i = 0

for burger, side, drink in zip(burgers, sides, drinks):
    total += int((burger + side + drink) * 0.9)
    i += 1

total += sum(burgers[i:]) + sum(sides[i:]) + sum(drinks[i:])

print(sum(burgers) + sum(sides) + sum(drinks))
print(total)
