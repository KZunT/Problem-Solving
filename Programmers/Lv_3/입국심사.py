def solution(n, times):
    answer = 0

    start = min(times)  # 최소 입국 시간
    end = max(times) * n  # 최대 입국 시간

    while start <= end:
        mid = (start + end) // 2  # 최적의 시간
        people = 0  # 심사를 통과한 사람의 수

        for time in times:
            people += mid // time  # 심사 통과

            if people >= n:  # 심사 통과자가 기준보다 많다면 break
                break

        if people >= n:  # 시간이 넘치는 경우
            end = mid - 1

        if people < n:  # 시간이 부족한 경우
            start = mid + 1

        answer = mid

    return answer