N = int(input())
num_list = []

for _ in range(N):
    num_list.append(str(input()))

for i in range(1, len(num_list[0]) + 1):
    results = []

    for j in range(N):
        if num_list[j][-i:] in results:
            break
        else:
            results.append(num_list[j][-i:])

    if len(results) == N:
        print(i)
        break
