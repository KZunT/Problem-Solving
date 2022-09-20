def solution(dartResult):
    result_list = []

    dartResult = dartResult.replace('10', 'k')

    num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "k"]
    bonus_list = ["S", "D", "T"]
    option_list = ["*", "#"]

    result = 0
    num = 0

    for idx in range(len(dartResult)):
        if dartResult[idx] in num_list:

            if dartResult[idx] == 'k':
                num = 10
            else:
                num = int(dartResult[idx])
            result_list.append(num)

        elif dartResult[idx] in bonus_list:
            if dartResult[idx] == "S":
                result_list[-1] = int(result_list[-1]) ** 1
            elif dartResult[idx] == "D":
                result_list[-1] = int(result_list[-1]) ** 2
            elif dartResult[idx] == "T":
                result_list[-1] = int(result_list[-1]) ** 3

        elif dartResult[idx] in option_list:
            if dartResult[idx] == "*":
                if len(result_list) == 1:
                    result_list[-1] = int(result_list[-1]) * 2
                else:
                    result_list[-1] = int(result_list[-1]) * 2
                    result_list[-2] = int(result_list[-2]) * 2
            elif dartResult[idx] == "#":
                result_list[-1] = int(result_list[-1]) * -1

    result = sum(result_list)

    return result