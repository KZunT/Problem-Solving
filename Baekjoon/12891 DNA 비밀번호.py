S, P = map(int, input().split())
DNA = list(input())
tmp = list(map(int, input().split()))
dic = {'A': tmp[0], 'C': tmp[1], 'G': tmp[2], 'T': tmp[3]}
base = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

count = 0
for i in range(S - P + 1):
    flag = True

    if i == 0:
        for j in range(P):
            base[DNA[j]] += 1
    else:
        base[DNA[i + P - 1]] += 1
        base[DNA[i - 1]] -= 1

    for j in ('A', 'C', 'G', 'T'):
        if base[j] < dic[j]:
            flag = False
            break

    if flag:
        count += 1

print(count)
