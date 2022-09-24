from typing import List
import re


def solution(k: int, dic: List[str], chat: str) -> str:
    answer = ''

    chat_list = chat.split(" ")
    word_list = chat.split(" ")

    # print(chat_list)

    for i in range(len(chat_list)):
        re_word = '[a-z]{1,' + str(k) + '}'

        word_list[i] = word_list[i].replace('.', re_word)

        p = re.compile(word_list[i])

        for w in dic:
            if p.match(w) != None:
                chat_list[i] = len(chat_list[i]) * '#'

    answer = " ".join(chat_list)

    return answer