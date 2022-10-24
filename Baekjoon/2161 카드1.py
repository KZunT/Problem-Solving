N = int(input())

card_list = [x for x in range(1, N+1)]
num_list = []

while len(card_list) > 1:
    num_list.append(card_list.pop(0))
    card_list.append(card_list.pop(0))

num_list.append(card_list[0])

print(*num_list)