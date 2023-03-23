N, start, end = map(int, input().split())

round_num = 0

while start != end:
    start -= start // 2
    end -= end // 2
    round_num += 1

print(round_num)
