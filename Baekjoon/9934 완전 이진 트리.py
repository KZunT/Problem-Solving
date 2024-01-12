K = int(input())
numbers = list(map(int, input().split()))

buildings = [[] for _ in range(K)]


def dfs(nodes, depth):
    mid = (len(nodes) // 2)

    buildings[depth].append(nodes[mid])

    if len(nodes) == 1:
        return

    dfs(nodes[:mid], depth + 1)
    dfs(nodes[mid + 1:], depth + 1)


dfs(numbers, 0)

for building in buildings:
    print(*building)
