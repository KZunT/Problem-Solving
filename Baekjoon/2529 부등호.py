def get_number(x, y, operation):
    if operation == '<':
        if x > y:
            return False
    else:
        if x < y:
            return False
    return True


def dfs(idx, num):
    if idx == K + 1:
        res.append(num)
        return

    for i in range(10):
        if not check[i]:
            if idx == 0 or get_number(num[idx - 1], str(i), operations[idx - 1]):
                check[i] = True
                dfs(idx + 1, num + str(i))
                check[i] = False


K = int(input())
operations = list(input().split())

check = [False] * 10
res = []
dfs(0, '')

res.sort()
print(res[-1])
print(res[0])
