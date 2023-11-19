input()

numbers = [int(i) for i in input().split()]

numbers.sort()

M = 0

if len(numbers) % 2 == 1:
    M = numbers.pop(-1)
answer = [numbers[i] + numbers[-i - 1] for i in range(len(numbers) // 2)]
answer.append(M)

print(max(answer))
