N = int(input())
coord = list(map(int, input().split()))
compression = list(set(sorted(coord)))
compression.sort()
comp_dict = dict()

for i, c in enumerate(compression):
    comp_dict[c] = i

for num in coord:
    print(comp_dict[num], end=' ')
