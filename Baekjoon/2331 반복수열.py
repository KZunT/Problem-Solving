A, P = map(int, input().split())
check = [A]

while True:
    again = 0
    for i in (str(check[-1])):
        again += int(i) ** P

    if again in check:
        break

    check.append(again)

print(check.index(again))
