N = int(input())
M = int(input())

vips = [int(input()) for _ in range(M)]

seat = [1, 1, 2]

for i in range(3, 41):
    seat.append(seat[i - 2] + seat[i - 1])
answer = 1

if M >= 1:
    pre = 0
    for i in range(0, M):
        answer = answer * seat[vips[i] - 1 - pre]
        pre = vips[i]
    answer = answer * seat[N - pre]
else:
    answer = seat[N]

print(answer)
