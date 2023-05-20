T = int(input())

for _ in range(T):
    N = int(input())
    tree = [int(x) for x in input().split()]
    tree.sort(reverse=True)

    result = 0
    for i in range(N - 2):
        result = max(result, tree[i] - tree[i + 2])

    print(result)
