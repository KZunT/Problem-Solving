from typing import List
import re

# 정규표현식 사용 , 아마 시간복잡도 문제가 있음

def solution(k: int, dic: List[str], chat: str) -> str:

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