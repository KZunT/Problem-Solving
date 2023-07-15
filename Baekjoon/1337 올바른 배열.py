N = int(input())
answer = 5
number = [int(input()) for _ in range(N)]

for i in range(N):
    cnt_1 = 4
    cnt_2 = 4
    for j in range(N):
        if number[i] + 5 > number[j] and number[i] < number[j]:
            cnt_1 -= 1
        elif number[i] - 5 < number[j] and number[i] > number[j]:
            cnt_2 -= 1
    answer = min(answer, cnt_1, cnt_2)

print(answer)
