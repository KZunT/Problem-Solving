N = int(input())

num = bin(N)[2:]

three, answer = 1, 0

for n in num[::-1]:
    answer += int(n) * three
    three *= 3

print(answer)
