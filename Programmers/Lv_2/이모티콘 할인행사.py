from itertools import product


def solution(users, emoticons):
    answer = []

    discount_percent = [10, 20, 30, 40]
    discount_list = list(product(discount_percent, repeat=len(emoticons)))

    for discount in discount_list:
        plus = 0
        total_price = 0
        for user in users:
            price = 0

            for idx, emoticon in enumerate(emoticons):
                if discount[idx] >= user[0]:
                    price += emoticon * (100 - discount[idx]) / 100

            if price >= user[1]:
                plus += 1
            else:
                total_price += price

            answer.append([plus, total_price])

    answer.sort(key=lambda x: (x[0], x[1]))

    return answer[-1]
