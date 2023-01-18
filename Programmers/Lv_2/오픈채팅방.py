def solution(record):
    answer = []
    user = dict()
    for m in record:
        if m.split()[0] == "Enter" or m.split()[0] == "Change":
            order, uid, nickname = m.split()
            user[uid] = nickname

    for m in record:
        if m.split()[0] == "Enter":
            answer.append(user[m.split()[1]] + "님이 들어왔습니다.")
        if m.split()[0] == "Leave":
            answer.append(user[m.split()[1]] + "님이 나갔습니다.")

    return answer