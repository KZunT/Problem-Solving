import calendar

def solution(a, b):
    day_list = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    idx = calendar.weekday(2016, a, b)
    answer = day_list[idx]
    return answer