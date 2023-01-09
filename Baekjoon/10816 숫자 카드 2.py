from collections import Counter

N = int(input())
card_list = list(map(int,input().split()))

M = int(input())
num_list = list(map(int,input().split()))

card_dict = Counter(card_list)

for n in num_list:
    print(card_dict[n], end=' ')