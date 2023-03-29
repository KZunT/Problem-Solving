N = int(input())

change = N % 5

if N == 1 or N == 3:
    print(-1)

elif change % 2 == 0:
    print((N // 5) + (change // 2))

else:
    print((N // 5) - 1 + (change + 5) // 2)