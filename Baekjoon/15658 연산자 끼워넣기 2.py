N = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_value = int(-1e9)
min_value = int(1e9)


def dfs(index, answer, plus, minus, mul, div):
    global max_value, min_value
    if index == N:
        max_value = max(max_value, answer)
        min_value = min(min_value, answer)
        return
    if plus > 0:
        dfs(index + 1, answer + numbers[index], plus - 1, minus, mul, div)
    if minus > 0:
        dfs(index + 1, answer - numbers[index], plus, minus - 1, mul, div)
    if mul > 0:
        dfs(index + 1, answer * numbers[index], plus, minus, mul - 1, div)
    if div > 0:
        dfs(index + 1, int(answer / numbers[index]), plus, minus, mul, div - 1)

init_value = numbers[0]

dfs(1, init_value, plus, minus, mul, div)

print(max_value)
print(min_value)
