import datetime

# 테스트 케이스 제외하고 런타임 에러 발생..

def solution(today, terms, privacies):

    answer = []

    terms_dict = {}
    today_list = list(map(int,today.split('.')))
    today_date = datetime.date(today_list[0], today_list[1], today_list[2])
    #print(today_date)

    for term in terms:
        term_list = term.split(' ')
        terms_dict[term_list[0]] = int(term_list[1])

    for i,privacy in enumerate(privacies):
        privacy_list = privacy.split(' ')
        privacy_date_list = list(map(int,privacy_list[0].split('.')))
        privacy_date = datetime.date(privacy_date_list[0], privacy_date_list[1], privacy_date_list[2])

        #print(privacy_date)

        d = (privacy_date_list[2] + (28 * terms_dict[privacy_list[1]])) % 28 - 1

        if d <= 0:
            d = d + 28
            m = (privacy_date_list[1] + ((privacy_date_list[2]+ (28 * terms_dict[privacy_list[1]])) // 28) - 1 ) % 12
            y = (privacy_date_list[0] + (privacy_date_list[1] + ((privacy_date_list[2]+ (28 * terms_dict[privacy_list[1]])) // 28) -1 ) // 12)
        else :
            m = (privacy_date_list[1] + ((privacy_date_list[2]+ (28 * terms_dict[privacy_list[1]])) // 28)) % 12
            y = (privacy_date_list[0] + (privacy_date_list[1] + ((privacy_date_list[2]+ (28 * terms_dict[privacy_list[1]])) // 28)) // 12)

        privacy_date_after = datetime.date(y,m,d)

        #print(privacy_date_after)

        #print(today_date > privacy_date_after)

        if today_date > privacy_date_after:
            answer.append(i+1)

    return answer