import itertools

N = int(input())

num_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if N >= 987654321:
    print(0)

flag = 0

for s in range(len(str(N)), len(str(N))+2):
    if flag == 1:
        break

    result = itertools.permutations(num_set, s)

    for i in result:

        num = ''.join(map(str, i))

        if int(num) > N:

            print(num)
            flag = 1
            break
