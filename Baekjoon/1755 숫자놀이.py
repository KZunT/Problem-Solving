M, N = map(int, input().split())

num_dict = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six',
            '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}

num_list = []

for i in range(M, N + 1):
    num_to_str = ' '.join([num_dict[j] for j in str(i)])
    num_list.append([i, num_to_str])

num_list.sort(key=lambda x: x[1])

for i in range(len(num_list)):
    if i % 10 == 0 and i != 0:
        print('')
    print(num_list[i][0], end=' ')
