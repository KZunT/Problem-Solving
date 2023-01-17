# def solution(phone_book):
#     dic = dict()

#     for p in phone_book:
#         for i in range(1, len(p)):  # 접두어 사전 만들기
#             dic[p[:i]] = 1

#     for p in phone_book:
#         if p in dic:  # 누군가 번호의 접두어라면
#             return False

#     return True

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):  # 정렬되어있는 문자기 때문에 바로 붙어있는 번호가 가장 유사함
        if p2.startswith(p1):
            return False
    return True