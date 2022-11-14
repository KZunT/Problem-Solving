K = int(input())

for i in range(K):

    grade = list(map(int, input().split()))
    del grade[0]
    grade.sort()

    diff = []
    print('Class', i+1)

    for i in range(len(grade) - 1):
        diff.append(grade[i + 1] - grade[i])

    print('Max', str(max(grade)) + ',', 'Min', str(min(grade)) + ',', 'Largest gap', max(diff))