def solution(n, arr1, arr2):
    answer = []

    b_arr = []

    for i, j in zip(arr1, arr2):
        binary = i | j
        b_arr.append(bin(binary)[2::])

    for idx, b in enumerate(b_arr):
        if len(b) < n:
            b_arr[idx] = "0" * (n - len(b)) + b

    for i in b_arr:
        i = i.replace("1", "#")
        i = i.replace("0", " ")
        answer.append(i)

    return answer

# 다시 풀어보는게 좋을것 같다.