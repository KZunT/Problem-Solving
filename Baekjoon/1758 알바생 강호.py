N = int(input())

tips = []
for _ in range(N):
    tips.append(int(input()))

tips.sort(reverse=True)

total = 0
for i in range(N):
    number = tips[i] - i
    if number < 0:
        break
    total += tips[i] - i

print(total)