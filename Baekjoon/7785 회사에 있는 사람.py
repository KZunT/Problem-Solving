N = int(input())

company = dict()

for _ in range(N):
    name, action = input().split()

    if action == 'enter':
        company[name] = 1
    else:
        del company[name]

for name in sorted(company.keys(), reverse=True):
    print(name)